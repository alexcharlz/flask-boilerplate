import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv

from config import config_by_name
from project_name.extensions import mail, bcrypt, db, migrate
from project_name import models

load_dotenv(find_dotenv())

# Configuration I used in Paywu App
# TODO: Refactor how you see fit
from config import config, Config


# Celery configuration
def create_celery():
    from celery import Celery, current_app

    celery = Celery(
        __name__,
        broker=Config.CELERY_BROKER_URL,
        backend=Config.CELERY_RESULT_BACKEND,
    )
    current_app.loader.import_default_modules()
    return celery


celery = create_celery()
# can separate each tasks by app
# i.e ["app_1.tasks", "app_2.tasks"]
# or just use the one in tasks folder
celery.autodiscover_tasks(["tasks"], force=True)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[os.getenv("ENV")])

    # initialize Flask Extensions here
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Celery configuration update
    celery.conf.update(app.config)

    # Celery Context
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    # Register Blueprints here
    from project_name.app_1 import app_1

    app.register_blueprint(app_1, url_prefix="/api/v1/app_1")

    return app
