from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if session['counter'] != 0:
        session['counter'] += 1

    else:
        session['counter'] = 0

    return render_template("index.html")
    print "am i working"
    # session['counter'] += 1

@app.route('/users', methods=['POST'])

def create_user():
    print "Got Post Info"

    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])
app.run(debug=True)
