from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    userID = db.Column(db.Integer, db.ForeignKey('user.id')) #define foreign key to associate each note with a user. here use lowercase first letter

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150)) #150 denotes the max characters in the string.
    password = db.Column(db.String(150))
    fname = db.Column(db.String(150))
    note = db.relationship('Note') #when defining relationship use uppercase on first letter