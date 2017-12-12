import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_URI = os.environ.get('DB_URI')
	

class TestingConfig(Config):
    TESTING = True
    DB_URI = os.environ.get('DB_URI')


class ProductionConfig(Config):
    DB_URI = os.environ.get('DB_URI')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
