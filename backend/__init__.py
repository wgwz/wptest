import os
from flask import Flask
from dotenv import load_dotenv
from .config import config
 

def create_app(config_name=None):
    app = Flask(__name__)

    _load_config(app, config_name=config_name)
    app.logger.info(app.config)
    
    return app


def _load_config(app, config_name=None):
    """load from .env if present, otherwise fallback on dev values.
    note that system environment variables will take precedence.
    see https://github.com/theskumar/python-dotenv#usages for more."""
    if config_name == 'production':
        prod_path = os.path.join(app.instance_path, '.env')
        load_dotenv(prod_path)
        app.config.from_object(config['production'])
    elif config_name == 'testing':
        test_path = os.path.join(app.instance_path, '.test-env')
        load_dotenv(test_path)
        app.config.from_object(config['testing'])
    else:
        default_path = os.path.join(app.root_path, '.dev-env')
        load_dotenv(default_path)
        app.config.from_object(config['default'])
    return None
