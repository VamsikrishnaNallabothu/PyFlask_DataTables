from flask import Flask, session, abort, request, make_response, redirect, render_template
from flask.ext.script import Manager
import os


app = Flask(__name__)
app.secret_key = os.urandom(26)


@app.route('/')
def index():
    session['user'] = "Vamsi"
    return '<h1>Good Request</h1>',200

'''@app.route('/user/<name>')
def user(name):
    #user_agent = request.headers.get('User-Agent')
    #return '<p>your browser is %s </p>' %user_agent
    return '<h1>Hello, %s!</h1>' %name'''

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirected')
def redirected():
    return redirect('http://www.example.com')

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'user not logged in'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Session Dropped!'


if __name__ == '__main__':
    app.run(debug=True)
