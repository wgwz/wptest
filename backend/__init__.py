import os
import logging
from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # load from .env if present, otherwise fallback on dev values
    # system environment variables take precedence.
    # see https://github.com/theskumar/python-dotenv#usages for more.
    dotenv_path = os.path.join(app.instance_path, '.env')
    load_dotenv(dotenv_path)
    app.config.from_object('backend.settings')

    return app
