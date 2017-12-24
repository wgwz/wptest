import os
from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_URI = os.environ.get('DB_URI')

    @staticmethod
    def load_conf(app):
        default_path = os.path.join(app.root_path, '.dev-env')
        load_dotenv(default_path)

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestingConfig(Config):
    TESTING = True
    DB_URI = os.environ.get('DB_URI')

    @staticmethod
    def load_conf(app):
        test_path = os.path.join(app.instance_path, '.test-env')
        load_dotenv(test_path)
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    DB_URI = os.environ.get('DB_URI')

    @staticmethod
    def load_conf(app):
        prod_path = os.path.join(app.instance_path, '.env')
        load_dotenv(prod_path)
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
