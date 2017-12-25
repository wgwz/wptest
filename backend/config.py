import os
from dotenv import load_dotenv


class ConfigLoadingError(Exception):
    pass


class Config:

    @staticmethod
    def load_env(base_dir, filename):
        config_path = os.path.join(base_dir, filename)
        if not load_dotenv(config_path):
            raise ConfigLoadingError(
                'Error loading config file: %s' % config_path
            )

    @classmethod
    def load_conf(cls, app):
        cls.SECRET_KEY = os.environ.get('SECRET_KEY')
        cls.API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    @classmethod
    def load_conf(cls, app):
        Config.load_env(app.root_path, '.dev-env')
        Config.load_conf(app)
        cls.DB_URI = os.environ.get('DB_URI')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestingConfig(Config):
    TESTING = True

    @classmethod
    def load_conf(cls, app):
        Config.load_env(app.instance_path, '.test-env')
        Config.load_conf(app)
        cls.DB_URI = os.environ.get('DB_URI')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):

    @classmethod
    def load_conf(cls, app):
        Config.load_env(app.instance_path, '.prod-env')
        Config.load_conf(app)
        cls.DB_URI = os.environ.get('DB_URI')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
