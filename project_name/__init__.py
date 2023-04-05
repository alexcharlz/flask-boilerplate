import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv

from config import config_by_name
from project_name.extensions import mail, bcrypt, db, migrate
from project_name import models

load_dotenv(find_dotenv())


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[os.getenv("ENV")])

    # initialize Flask Extensions here
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Register Blueprints here
    from project_name.app_1 import app_1

    app.register_blueprint(app_1, url_prefix="/api/v1/app_1")

    return app
