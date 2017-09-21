# Import flask dependencies
from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

# Handle HTTP error
@routes.errorhandler(404)
def not_found(erro):
    return render_template('404.html'), 404

@routes.route('/')
def index():
    return  render_template('index.html')
