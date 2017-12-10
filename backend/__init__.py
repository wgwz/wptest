import os
from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # load from .env if present, otherwise fallback on dev values.
    # note that system environment variables will take precedence.
    # see https://github.com/theskumar/python-dotenv#usages for more.
    dotenv_path = os.path.join(app.instance_path, '.env')
    if load_dotenv(dotenv_path):
        app.config.from_object('backend.prod_settings')
    else:
        app.config.from_object('backend.dev_settings')

    app.logger.info(app.config)

    return app
