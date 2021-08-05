import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import app_config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name=os.environ.get('CONFIG_NAME', 'development')):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from app.pets import  bp as pets_bp
    app.register_blueprint(pets_bp)

    from app.commons import bp as commons_bp
    app.register_blueprint(commons_bp)

    return app
