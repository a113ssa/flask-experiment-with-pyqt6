from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import GameRequestSchema, GameResponseSchema
from src.chatbot.chatbot import Chatbot

from langchain_core.messages import SystemMessage, HumanMessage

blp = Blueprint("Games", __name__, description="Game operations")
chat = Chatbot()


@blp.route("/games")
class Games(MethodView):
    @blp.response(200)#, GameResponseSchema)
    def get(self):
        response = chat.send_message([SystemMessage('Start New Game')])
        return response

    @blp.arguments(GameRequestSchema)
    @blp.response(200, GameResponseSchema)
    def post(self, request_data):
        response = chat.send_message([HumanMessage(request_data['message'])])
        return response
