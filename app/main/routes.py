from . import main_blueprint
from flask import render_template

@main_blueprint.route('/')
def home():
    return render_template('main/home.html')