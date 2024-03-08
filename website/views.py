from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/') #<--whenever website hits this route it calls the function below
def home():
    return "<h1>Sample Text</h1>"