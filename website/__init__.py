from flask import Flask

def CreateApp():
    app = Flask(__name__) #initializes flask
    app.config['SECRET_KEY'] = 'AdamTroup' #creates key to encrypt cookies & session data

    from .views import views #import blueprints. from FILE views.py import this variable "views = Blueprint('views', __name__)"
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #register each blueprint to the "/" endpoint
    app.register_blueprint(auth, url_prefix='/')

    return app

