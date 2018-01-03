# project/__init__.py


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


# instantiate the db
db = SQLAlchemy()
mail = Mail()


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # Mail setting
    mail.init_app(app)

    # register blueprints
    from server.views.temp import user_blueprint
    from server.views.auth import auth_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
