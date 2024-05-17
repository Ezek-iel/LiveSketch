from config import config_dict
from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()

def create_app(config = os.getenv('APP_CONFIG')):
    
    #* Create app and add config
    app = Flask(__name__)
    app.config.from_object(config_dict[config])

    #* Initialize extensions
    
    #* register blueprints
    from .users import user_blueprint
    app.register_blueprint(blueprint = user_blueprint, url_prefix = '/users')

    return app
