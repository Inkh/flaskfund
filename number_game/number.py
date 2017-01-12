from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods = ['POST', 'GET'])
def index():

    # print random.randrange(0,101)
    session['num'] = random.randrange(0,101)
    print session['num']
    return render_template("index.html", result = "Guess now!")

@app.route('/guesser', methods = ['POST'])
def guessing():
    # session['guess'] = request.form['guess']
    print session['num']
    print request.form['guess']
    randNum = session['num']
    userNum = request.form['guess']
    print userNum < randNum
    if userNum > randNum:
        print "huzzah"
    elif userNum < randNum:
        print "nope"
    # if request.form['guess'] > session['num']:
    #     return redirect('/low')
    # elif int(session['guess']) < session['num']:
    #     return redirect('/high')
    # elif int(session['guess']) == session['num']:
    #     return redirect('/nice')
    return render_template("index.html")

@app.route('/high')
def high():
    return render_template("index.html")

@app.route('/low')
def low():
    result = "Lower!"
    return render_template('index.html', result = "Lower")

@app.route('/nice')
def nice():
    result = "You got it!"
    return render_template("index.html", result = "You got it!")
app.run(debug=True)
