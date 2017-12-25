import os
from dotenv import load_dotenv


class Config:

    @classmethod
    def load_conf(cls, app):
        cls.SECRET_KEY = os.environ.get('SECRET_KEY')
        cls.API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    @classmethod
    def load_conf(cls, app):
        config_path = os.path.join(app.root_path, '.dev-env')
        load_dotenv(config_path)
        Config.load_conf(app)
        cls.DEBUG = True
        cls.DB_URI = os.environ.get('DB_URI')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestingConfig(Config):

    @classmethod
    def load_conf(cls, app):
        config_path = os.path.join(app.instance_path, '.test-env')
        load_dotenv(config_path)
        Config.load_conf(app)
        cls.TESTING = True
        cls.DB_URI = os.environ.get('DB_URI')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    DB_URI = os.environ.get('DB_URI')

    @staticmethod
    def load_conf(app):
        config_path = os.path.join(app.instance_path, '.env')
        load_dotenv(config_path)
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
