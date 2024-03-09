from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST']) #http://127.0.0.1:5000/login // the GET POST allows the http request to accept both, only get is default
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() #search for row by email. Usually emails would be unique, but here to keep from breaking i use .first() to return the first result
        if user: #if a matching user exists
            if check_password_hash(user.password, password): #compare the db password with the password above
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else: #if no mathcing users exist
            flash('No account associated with this email', category='error')

    data = request.form
    return render_template('login.html', user=current_user) #pass data like the 'text' here. you can pass multiple variables

@auth.route('/logout',  methods = ['GET', 'POST']) #http://127.0.0.1:5000/logout
@login_required #cannot access log out if not already logged in
def lougout():
    logout_user()
    flash('Logged out successfully', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/signup',  methods = ['GET', 'POST']) #http://127.0.0.1:5000/signup
def signup():
    if request.method == 'POST': #only access this code if the endpoint receives a post request
        email = request.form.get('email')
        fname = request.form.get('fname') #similar to accessing a field from a json object
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        #error handling for user input
        #add block from submitting if field is empty
        #only reset password when an alert is triggered, it seems to refresh the page now
        user = User.query.filter_by(email=email).first() #search for row by email. Usually emails would be unique, but here to keep from breaking i use .first() to return the first result
        if user: #if the user's email input already exists in the db
            flash('Account with email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 3 characters', category='error')
        elif len(fname) < 2:
            flash('Name must be longer than 1 character', category='error')
        elif password != confirmPassword: #keeps case sensitivity
            flash('Passwords do not match', category='error')
        elif len(password) < 6:
            flash('Password must be 6 characters or longer', category='error')
        else:
            newUser = User(email=email, fname=fname, password=generate_password_hash(password, method='pbkdf2'))
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True) #sign in after they create account
            flash('Account created successfully', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)