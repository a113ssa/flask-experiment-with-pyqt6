from flasgger import Swagger
from flask import Flask, request

from src.chatbot.chatbot import GeminiChatbot as chatbot

app = Flask(__name__)
swagger = Swagger(app)
chat = chatbot()

@app.get('/chatbot')
def get_chatbot():
    """Endpoint to init game
    Send message to start new game
    ---
    parameters:
        - name: message
          in: body
          required: true
          schema:
                type: object
                properties:
                    message:
                        type: string
                        example: 'Start New Game'
    responses:
      200:
        description: Initial game response
        schema:
            type: object
            properties:
                questText:
                    type: string
                    example: 'You are in a dark room. What do you do?'
                responseVariants:
                    type: array
                    items:
                        type: string
                mood:
                    type: string
        examples:
            questText: 'You are in a dark room. What do you do?'
            responseVariants: ['Turn on the light', 'Open the door', 'Scream']
            mood: 'neutral'
    """
    response = chat.send_message('Start New Game')
    return  response

@app.post('/chatbot')
def post_chatbot():
    """Endpoint to send message
    Send message to chatbot
    ---
    parameters:
      - name: message
        in: body
        required: true
        schema:
            type: object
            properties:
                message:
                    type: string
                    example: 'Turn on the light'
    responses:
        200:
            description: Chatbot response
            schema:
                type: object
                properties:
                    questText:
                        type: string
                        example: 'You are in a dark room. What do you do?'
                    responseVariants:
                        type: array
                        items:
                            type: string
                    mood:
                        type: string
            examples:
                questText: 'You are in a dark room. What do you do?'
                responseVariants: ['Turn on the light', 'Open the door', 'Scream']
                mood: 'neutral'
        """
    request_data = request.get_json()
    response = chat.send_message(request_data['message'])
    return response
