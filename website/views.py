from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/') #<--whenever website hits this route it calls the function below
@login_required #cant access home page unless youre logged in
def home():
    return render_template('home.html', user=current_user) #calls the home.html template to populate the screen when this route function is called