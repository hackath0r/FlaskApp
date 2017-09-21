# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Import db module from mod_db
from app.mod_db.models import db

# Connect SQLAlchemy object to application
db.init_app(app)
db.app = app

# Handle HTTP error
@app.errorhandler(404)
def not_found(erro):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return  render_template('index.html')

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()


