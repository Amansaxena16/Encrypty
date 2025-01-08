from flask import Flask, render_template, request
from main import encryptFile, decryptFile
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        path = request.form.get('path')
        operation = request.form.get('operation')
        print(operation)
        
        if path == "":
            return render_template('index.html',error = "No File Selected")
        
        if operation == "encrypt":
            encryptFile(path)
            return render_template('index.html',message = "File Encrypted Successfully")
        else:
            decryptFile(path)
            return render_template('index.html',message = "File Decrypted Successfully")
    return render_template('index.html')


if __name__ == '__main__':  
   app.run(debug=True)  # Run the app in debug mode