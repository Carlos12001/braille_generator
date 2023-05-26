from flask import Flask, request, jsonify
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw() # part of the import if you are not using other tkinter functions

fpath = None
fcontent = None

def setFPath(path):
    global fpath
    fpath = path

def setFContent(content):
    global fcontent
    fcontent = content

app = Flask(__name__)

@app.route('/test')
def hello():
    return "Soy la mazacuata, la python!"

@app.route('/process-file', methods=['POST'])
def process_file():
    file_path = request.data.decode('utf-8')
    setFPath(file_path)

    # Perform processing on the file content
    with open(file_path, 'r') as file:
        file_content = file.read()
        setFContent(file_content)

    # Example: Print the file content
    print(file_content)

    # Send a response back to JavaScript
    response = 'got it'
    return file_content


@app.route('/save-file', methods=['POST'])
def save_file():
    if(fpath):
        file_content = request.data.decode('utf-8')
        setFContent(file_content)
        with open(fpath, 'w') as file:
            file.write(fcontent)
        
        return "Saved file successfully"

    else:
        return "Error: Open a file first!"

@app.route('/', methods = ['Get'])
def get_text():
    return jsonify({"read":"text"})

app.run()

if __name__ == "__main__":
    #app.run(debug=True)
    app.run()