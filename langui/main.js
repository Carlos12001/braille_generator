const { app, BrowserWindow, Menu, ipcMain, dialog } = require('electron')
const path = require('path')
//const axios = require('axios')
//const pylink = require('./src/backend/pylink.js');
//const { dialog } = require('electron');

const createWindow = () => {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      //webSecurity: false, // Disable web security for development only
      //contentSecurityPolicy: "default-src 'self' http://localhost:5000",
    },
  })

  win.loadFile('src/ui/index.html')


 

  //Se usa para hacer debug y ver los console.log
  //win.webContents.openDevTools()

  
  let menu = Menu.buildFromTemplate([])
  Menu.setApplicationMenu(menu)
}

ipcMain.handle('open-file-dialog', async (event) => {
  const result = await dialog.showOpenDialog({
    properties: ['openFile'],
  });

  return { filePaths: result.filePaths };
});


// Espera a que el modulo app este listo antes de crear la ventana. 
app.whenReady().then(() => {
  createWindow()



  //Carga el flask como un chamaquito
  var python = require('child_process').spawn('py', ['./src/app.py']);
  python.stdout.on('data', function (data) {
    console.log("data: ", data.toString('utf8'));
  });
  python.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`); // when error
  });

  // Esto es para mac, se asegura de crear ventana si el proceso existe pero no hay ventanas
  // abiertas.
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Se asegura de que terminar el proceso si todas las ventanas estan cerradas. (win/linux)
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})