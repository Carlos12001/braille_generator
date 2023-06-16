const { ipcRenderer } = require('electron');

const openf = document.getElementById("open")
const save = document.getElementById("save")
const compile = document.getElementById("compile")
const run = document.getElementById("run")

const editor = document.getElementById("editor")
const consolet = document.getElementById("console")

let filePath = null;

/*

save.addEventListener('click', async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/test');
    if (response.ok) {
      const data = await response.text();
      console.log('It says:', data);
    } else {
      console.log('Request failed:', response.status);
    }
  } catch (error) {
    console.log('Error:', error);
  }
});
*/


function cleanConsole(){
  consolet.value = "";
}

function updateConsole(text){
  consolet.value = text;
}



save.addEventListener('click', async () => {
  const editorValue = editor.value; // Get the text from the editor

  if (filePath !== null) {
    // Replace the file's text with the editor's text
    const response = await fetch('http://127.0.0.1:5000/save-file', {
    method: 'POST',
    body: editor.value,
    });

    const data = await response.text();
    updateConsole(data);
    console.log(data); // Print the response from Python
  }
});


compile.addEventListener('click', async () => {
  if (filePath !== null) {
    // Replace the file's text with the editor's text
    const response = await fetch('http://127.0.0.1:5000/compile-file', {
    method: 'GET',
    });

    const data = await response.text();
    updateConsole(data);
    console.log(data); // Print the response from Python
  }

   else {
    updateConsole("Open a file first!")
  }
});


run.addEventListener('click', async () => {
  if (filePath !== null) {
    // Replace the file's text with the editor's text
    const response = await fetch('http://127.0.0.1:5000/run-file', {
    method: 'GET',
    });

    const data = await response.text();
    updateConsole(data);
    console.log(data); // Print the response from Python
  }
  else {
    updateConsole("Open a file first!");
  }
});


openf.addEventListener('click', () => {
  cleanConsole();
  ipcRenderer.invoke('open-file-dialog')
    .then((result) => {
      filePath = result.filePaths[0];

    fetch('http://127.0.0.1:5000/process-file', {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain',
      },
      body: filePath,
    })
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        editor.value = data;
      })
      //errors while doing HTTP request
      .catch((error) => {
        console.log(error);
      });
    //Errors while opening file
  }).catch((err) => {
    console.log(err);
  });
});

/*
openf.addEventListener('click', () => {
  // Create a file input element
  const fileInput = document.createElement('input');
  fileInput.type = 'file';

  // Add event listener to handle file selection
  fileInput.addEventListener('change', async (event) => {
    const file = event.target.files[0]; // Get the selected file

    fileContent = await readFileContent(file); // Read the file content

    // set editor text to file text
    editor.value = fileContent;

    // Send the file content to Python
    const response = await sendFileContentToPython(fileContent);

    console.log(response); // Print the response from Python
  });

  // Trigger the file explorer
  fileInput.click();
});

// Function to read the file content
function readFileContent(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = (event) => {
      const content = event.target.result;
      resolve(content);
    };

    reader.onerror = (error) => {
      reject(error);
    };

    reader.readAsText(file);
  });
}


//first iteration
// Function to send the file content to Python
async function sendFileContentToPython(fileContent) {
  const response = await fetch('/process-file', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ fileContent }),
  });

  const data = await response.json();

  return data;
}
*/

// Function to send the file content to Python
async function sendFileContentToPython(fileContent) {
  //console.log(fileContent);

  const response = await fetch('http://127.0.0.1:5000/process-file', {
    method: 'POST',
    body: fileContent,
  });

  const data = await response.text();

  return data;
}