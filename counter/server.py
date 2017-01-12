from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if session.has_key('counter'):
        session['counter'] += 1
    else:
        session['counter'] = 1

    return render_template("index.html")

@app.route('/reset', methods = ['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

@app.route('/plusTwo', methods = ['POST'])
def plusTwo():
    session['counter'] += 1
    return redirect('/')

app.run(debug=True)
