from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def three():
    return render_template("playground.html", times=3)

@app.route('/play/<int:num>')
def repeat(num):
    return render_template("playground.html", times=num)

@app.route('/play/<int:num>/<color>')
def changecolor(num, color):
    return render_template("playground.html", times=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)


