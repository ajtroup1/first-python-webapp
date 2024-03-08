from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login') #http://127.0.0.1:5000/login
def login():
    return "<h1>Login</h1>"

@auth.route('/logout') #http://127.0.0.1:5000/logout
def lougout():
    return "<h1>Logout</h1>" 

@auth.route('/signup') #http://127.0.0.1:5000/signup
def signup():
    return "<h1>Sign Up</h1>"