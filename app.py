from flask import Flask, render_template,request,send_file
from main import encryptFile, decryptFile
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        operation = request.form.get('operation')

        print(file)
    return render_template('index.html')


if __name__ == '__main__':  
   app.run(debug=True)  # Run the app in debug mode