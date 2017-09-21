# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object 
db = SQLAlchemy(app)

# Handle HTTP error
@app.errorhandler(404)
def not_found(erro):
    return render_template('404.html'), 404

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()


