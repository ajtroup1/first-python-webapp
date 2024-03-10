from flask import Blueprint, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) #<--whenever website hits this route it calls the function below
@login_required #cant access home page unless youre logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            newNote = Note(text=note, userID = current_user.id, complete=False) #create the Note object from models.py
            db.session.add(newNote)
            db.session.commit()
            flash('Note added successfully', category='success')


    return render_template('home.html', user=current_user) #calls the home.html template to populate the screen when this route function is called