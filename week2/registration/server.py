from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
EMAIL_RE = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_RE = re.compile(r'^(?=.*?[A-Z])(?=.*?[0-9])')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    errors = True
    msg = ""

    if len(request.form['firstname']) == 0:
        msg = "Enter first name"
    elif len(request.form['lastname']) == 0:
        msg = "Enter last name"
    elif len(request.form['email']) == 0:
        msg = "Enter email"
    elif len(request.form['email']) < 8:
        msg = "Email should be atleast 8 characters long"
    elif not PASSWORD_RE.match(request.form['password']):
        msg = "Enter valid password"
    elif not EMAIL_RE.match(request.form['email']):
        msg = "Enter valid email"
    elif request.form['password'] != request.form['confirmpassword']:
        msg = "Password should match"
    else:
        errors = False
        
    if errors==True:
        flash(msg, "error")
    else:
        flash('Successful Registration!', 'success')

    return redirect('/')

app.run(debug=True)

