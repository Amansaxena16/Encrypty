from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        path = request.form.get('path')
        operation = request.form.get('operation')
        
        print(path,operation)
    return render_template('index.html')


if __name__ == '__main__':  
   app.run(debug=True)  # Run the app in debug mode