from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "keep_it_simple"

@app.route('/')
def index():
    if 'target' not in session:
        session['target'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        val1 = int(request.form['guess'])
    except:
        return redirect('/')
    if session['target'] == val1:
        session['result'] = 'correct'
    elif session['target'] > val1:
        session['result'] = 'less'
    elif session['target'] < val1:
        session['result'] = 'high'
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('target')
    session.pop('result')
    return redirect('/')

app.run(debug=True)    