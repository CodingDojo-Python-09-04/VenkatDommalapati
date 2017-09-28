from flask import Flask, render_template, session, redirect, flash, request
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=[ 'POST'])
def process():
    errors = False
    if len(request.form['name']) == 0:
        flash("Please enter name")
        errors = True
    elif len(request.form['comment']) == 0:
        flash("Please enter comments")
        errors = True
    elif len(request.form['comment']) > 120:
        flash("Comments are too big")
        errors = True
    if errors:
        return redirect('/')
    session['result_info'] = request.form
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html", result=session['result_info'])

app.run(debug=True)
    