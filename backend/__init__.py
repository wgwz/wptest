import os
from flask import Flask
from dotenv import load_dotenv
from .config import config
 

def create_app(config_name=None):
    app = Flask('wptest')

    _load_config(app, config_name=config_name)
    app.logger.info(app.config)
    
    return app


def _load_config(app, config_name=None):
    config[config_name or 'default'].load_conf(app)
    app.config.from_object(config[config_name or 'default'])
    return None
