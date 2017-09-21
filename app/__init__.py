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

# Import routes blueprint
from routes import routes

# Register blueprint(s)
app.register_blueprint(routes)

# Connect SQLAlchemy object to application
db.init_app(app)
db.app = app

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()


