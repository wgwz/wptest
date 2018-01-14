import os
from flask import Flask
from werkzeug.utils import find_modules, import_string
from .config import config
from distutils.sysconfig import get_python_lib

__version__ = '0.0dev'


def create_app(config_name=None):
    app = Flask('wptest', static_folder='static')

    _load_config(app, config_name=config_name)
    app.logger.info(app.config)
    _register_blueprints(app)

    return app


def _load_config(app, config_name=None):
    config[config_name or 'default'].load_conf(app)
    app.config.from_object(config[config_name or 'default'])
    return None


def _register_blueprints(app):
    """Automagically register all blueprint packages

    Just take a look in the blueprints directory.
    """
    for name in find_modules('backend', recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None
