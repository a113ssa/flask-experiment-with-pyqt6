from flask import Flask
from flask_smorest import Api

from resources.game import blp as GameBlueprint


class ApiConfig:
    API_TITLE = 'Text Quest Adventure Game'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/api-docs'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

app = Flask(__name__)

app.config.from_object(ApiConfig)

api = Api(app)

api.register_blueprint(GameBlueprint)
