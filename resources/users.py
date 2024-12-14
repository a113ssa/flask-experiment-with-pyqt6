from flask.views import MethodView
from flask_smorest import Blueprint

from models import UserModel
from schemas import UserRequestSchema, UserResponseSchema

blp = Blueprint("User", __name__, description="User operations")

DEFAULT_HEALTH = 100


@blp.route("/users")
class Users(MethodView):
  @blp.arguments(UserRequestSchema)
  @blp.response(200, UserResponseSchema)
  def post(self, request_data):
     user = UserModel(**request_data, health=DEFAULT_HEALTH)
     return user