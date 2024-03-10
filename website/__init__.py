from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask import current_app
from flask_login import LoginManager

db = SQLAlchemy() #this is the actual database object
DB_NAME = 'database.db'

def CreateApp():
    app = Flask(__name__) #initializes flask
    app.config['SECRET_KEY'] = 'AdamTroup' #creates key to encrypt cookies & session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #automatically looks for the primary key here

    from .views import views #import blueprints. from FILE views.py import this variable "views = Blueprint('views', __name__)"
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #register each blueprint to the "/" endpoint
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    CreateDatabase(app)

    return app

def CreateDatabase(app):  # create database if it doesn't exist
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created database***')
