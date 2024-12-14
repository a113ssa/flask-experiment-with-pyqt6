from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import UserModel
from schemas import UserRequestSchema, UserResponseSchema, UserUpdateRequestSchema

blp = Blueprint("Users", __name__, description="User operations")

DEFAULT_HEALTH = 100


@blp.route("/users")
class Users(MethodView):
  @blp.arguments(UserRequestSchema)
  @blp.response(200, UserResponseSchema)
  def post(self, request_data):
    user = UserModel(**request_data, health=DEFAULT_HEALTH)

    try:
      db.session.add(user)
      db.session.commit()
    except SQLAlchemyError:
      abort(422, "User already exists")

    return user

  @blp.response(200, UserResponseSchema(many=True))
  def get(self):
    users = UserModel.query.all()

    return users

@blp.route("/users/<int:user_id>")
class User(MethodView):
  @blp.response(200, UserResponseSchema)
  def get(self, user_id):
    print(user_id)
    user = UserModel.query.get_or_404(user_id)

    return user


  @blp.arguments(UserUpdateRequestSchema)
  @blp.response(200, UserResponseSchema)
  def put(self, request_data, user_id):
    user = UserModel.query.get_or_404(user_id)

    user.health = request_data['health']
    db.session.commit()

    return user


  @blp.response(204)
  def delete(self, user_id):
    user = UserModel.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return 204
