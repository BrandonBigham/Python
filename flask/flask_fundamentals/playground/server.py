from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def sayname(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<word>')
def repeat(num,word):
    return num * word



if __name__ == "__main__":
    app.run(debug=True)