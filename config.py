from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY")

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URI")

class TestingConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URI")

class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DATABASE_URI")

config_dict = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'default' : DevelopmentConfig
}

    