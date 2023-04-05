import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = False
    # MAIL
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
    MAIL_USE_TLS = bool(int(os.getenv("MAIL_USE_TLS")))
    MAIL_USE_SSL = bool(int(os.getenv("MAIL_USE_SSL")))
    # DATABASE
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(development=DevelopmentConfig, production=ProductionConfig)
