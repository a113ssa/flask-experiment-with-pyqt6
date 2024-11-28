from flask import Flask, request

from src.chatbot.chatbot import GeminiChatbot as chatbot

app = Flask(__name__)
chat = chatbot()

@app.get('/chatbot')
def get_chatbot():
    response = chat.send_message('Start New Game')
    return  response

@app.post('/chatbot')
def post_chatbot():
    request_data = request.get_json()
    response = chat.send_message(request_data['message'])
    return response
