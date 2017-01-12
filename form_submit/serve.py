from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

# @app.route('/', methods=['POST','GET'])

# def create_user():
#     print "Got Post Info"
#
#     name = request.form['name']
#     email = request.form['email']
#
#     return redirect('/direct')


@app.route('/direct', methods=['POST'])

def something():
    return render_template("direct.html", name = request.form['name'], email = request.form['email'], language = request.form["language"], location = request.form["loc"], comments = request.form['comments'])

app.run(debug=True)
