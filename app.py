from flasgger import Swagger
from flask import Flask
from flask_smorest import Api

from resources.game import blp as GameBlueprint

app = Flask(__name__)
swagger = Swagger(app)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = 'Text Quest Adventure Game'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/'

api = Api(app)

api.register_blueprint(GameBlueprint)
