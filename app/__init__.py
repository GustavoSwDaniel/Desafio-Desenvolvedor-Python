import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()


def create_app(config_name=os.environ.get('CONFIG_NAME', 'development')):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    CORS(app)

    return app
