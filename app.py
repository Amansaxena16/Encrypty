from flask import Flask, render_template,request,send_file
from main import encryptFile, decryptFile
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        operation = request.form.get('operation')
        print(operation)
        
        if not file:
            return render_template('index.html',error = "No File Selected")
        
        path = os.path.join('uploads',file.filename)
        file.save(path)
        
        if operation == "encrypt":
            encryptFile(path)
            process_file_path = path
        else:
            decryptFile(path)
            process_file_path = path
        return send_file(process_file_path, as_atachment=True)
    return render_template('index.html')


if __name__ == '__main__':  
   app.run(debug=True)  # Run the app in debug mode