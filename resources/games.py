from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import GameRequestSchema, GameResponseSchema
from src.chatbot.chatbot import GeminiChatbot as chatbot

blp = Blueprint("Game", __name__, description="Game operations")
chat = chatbot()


@blp.route("/games")
class Games(MethodView):
    @blp.response(200, GameResponseSchema)
    def get(self):
        response = chat.send_message('Start New Game')
        return response

    @blp.arguments(GameRequestSchema)
    @blp.response(200, GameResponseSchema)
    def post(self, request_data):
        response = chat.send_message(request_data['message'])
        return response
