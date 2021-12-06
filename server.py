import re
from flask import Flask, render_template, request, redirect, session, sessions


app = Flask(__name__)
app.secret_key = "survey"

@app.route('/')
def disp_survey():
    return render_template ('dashboard.html',)


@app.post('/process')
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']

    session['name'] = name
    session['location'] = location
    session['language'] = language
    # store data in a database
    # log a user in based on credentials
    # compare input values
    return redirect('/results')

@app.route('/results')       
def result():
    return render_template("results.html")

@app.route('/goback', methods=['POST'])
def go_back():
    return redirect('/')



# @app.route('/clear')
# def clear_session():
#     print('surey cleared from session')
#     del session['name']
#     del session['location']
#     del session['language']

    session.clear()
    
    # return redirect('/')


if __name__ == '__main__':
    app.run(port=8000,debug=True)