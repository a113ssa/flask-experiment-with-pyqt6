import os

from flask import Flask
from flask_smorest import Api

from db import db
from resources.games import blp as GameBlueprint
from resources.users import blp as UserBlueprint


class ApiConfig:
    API_TITLE = 'Text Quest Adventure Game API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/api-docs'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)

app.config.from_object(ApiConfig)
with app.app_context():
    db.init_app(app)
    db.create_all()

api = Api(app)

api.register_blueprint(GameBlueprint)
api.register_blueprint(UserBlueprint)
