from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "jahfiuebf"
@app.route('/')
def home():
    if 'gold' not in session:
        session["gold"] = 0
        session['activity']=[]
    return render_template("gold.html")

@app.route('/process/gold', methods=['post'])
def process():
    if request.form["building"] == "Farm":
        temp = random.randint(10,20)
        session['gold'] += temp
        session['activity'].append("you gained " + str(temp) + " gold")
    if request.form["building"] == "Cave":
        temp = random.randint(5,10)
        session['gold'] += temp
        session['activity'].append("you gained " + str(temp) + " gold")
    if request.form["building"] == "House":
        temp = random.randint(-5,-2)
        session['gold'] += temp
        session['activity'].append("you lost " + str(-temp) + " gold")
    if request.form["building"] == "Casino":
        temp = random.randint(-1000,1000)
        session['gold'] += temp
        if temp > 0:
            session['activity'].append("you gained " + str(temp) + " gold")
        if temp < 0:
            session['activity'].append("you lost " + str(-temp) + " gold")
    if request.form["building"] == "reset":
        session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)