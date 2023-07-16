from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    # Creating the flask app object - this is the core of the app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")

    # creating database object! This allows the use of ORM
    db.init_app(app)

    # creating marshmallow object! This allows the use of schemas
    ma.init_app(app)

    # creating the jwt and bcrypt objects! this allows the use of authentication
    bcrypt.init_app(app)
    jwt.init_app(app)

    # WILL ACTIVATE LATER
    # from commands import db_commands
    # app.register_blueprint(db_commands)

    # # import the controllers and activate the blueprints
    # from controllers import registerable_controllers

    # for controller in registerable_controllers:
    #     app.register_blueprint(controller)

    return app
