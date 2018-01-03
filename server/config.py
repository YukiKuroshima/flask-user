# project/config.py


import server.instance.secret
import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = server.instance.secret.SECRET_KEY
    RECAPTCHA_PUBLIC_KEY = server.instance.secret.RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_PRIVATE_KEY = server.instance.secret.RECAPTCHA_PRIVATE_KEY
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = server.instance.secret.MAIL_USERNAME
    MAIL_PASSWORD = server.instance.secret.MAIL_PASSWORD


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
