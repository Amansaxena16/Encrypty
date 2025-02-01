from flask import Flask, render_template,request,send_file
from main import encryptFile, decryptFile
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        operation = request.form.get('operation')
        
        if file:
            uploadFile = os.path.join('uploads',file.filename)
            file.save(uploadFile)
            
        if not file or operation:
            return render_template('index.html',error="Try Again!! Error") 
        
        if operation == "encrypt":
            encryptFile(uploadFile)
        else:
            decryptFile(uploadFile)
    
    return render_template('index.html')


if __name__ == '__main__':  
   app.run(debug=True)  # Run the app in debug mode