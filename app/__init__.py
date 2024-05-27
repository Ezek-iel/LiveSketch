from config import config_dict
from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def redirect_home():
    #* Redirect to home page
    
    from flask import redirect, url_for
    return redirect(url_for('main.home'))

load_dotenv()

def create_app(config = os.getenv('APP_CONFIG')):
    
    #* Create app and add config
    app = Flask(__name__)
    app.config.from_object(config_dict[config])

    #* Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    #* register blueprints
    from .users import user_blueprint
    app.register_blueprint(blueprint = user_blueprint, url_prefix = '/users')

    from .main import main_blueprint
    app.register_blueprint(blueprint = main_blueprint, url_prefix = '/main')

    from .room import room_blueprint
    app.register_blueprint(blueprint = room_blueprint, url_prefix = '/room')

    from .auth import auth_blueprint
    app.register_blueprint(blueprint = auth_blueprint, url_prefix = '/auth')

    app.add_url_rule('/', 'home', redirect_home)

    from app import models
    from app import documents

    return app
