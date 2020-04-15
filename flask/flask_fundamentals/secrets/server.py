from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('secret.html')

@app.route('/tell_secret', methods=["POST"])
def tell_secret():
    print(request.form['secret'])
    return render_template('the_secret.html', the_secret=request.form['secret'])

if __name__ == "__main__":
    app.run(debug=True)