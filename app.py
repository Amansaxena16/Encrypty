from flask import Flask, render_template,request,send_file, redirect,url_for
from main import encryptFile, decryptFile
import os
app = Flask(__name__)

MAX_FILE_SIZE = 10 * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        operation = request.form.get('operation')
        
        if file:
            uploadFile = os.path.join('uploads',file.filename)
            file.save(uploadFile)
            
        fileSize = os.path.getsize(uploadFile)
        if fileSize > MAX_FILE_SIZE:
            os.remove(uploadFile)
            return render_template('index.html',error="File Size should be under 10MB") 
            
        if not file or not operation:
            return render_template('index.html',error="Try Again!! Error") 
        
        if operation == "encrypt":
            encryptFile(uploadFile)
            # os.remove(file)
            return redirect(url_for('download',filePath=uploadFile,operation=operation))
        else:
            decryptFile(uploadFile)    
            return redirect(url_for('download',filePath=uploadFile,operation=operation))
    
    return render_template('index.html')


@app.route("/download")
def download():
    path = request.args.get('filePath')
    response = send_file(path, as_attachment=True)
    os.remove(path)
    return response


if __name__ == '__main__':  
   app.run(debug=True)  # Run the app in debug mode