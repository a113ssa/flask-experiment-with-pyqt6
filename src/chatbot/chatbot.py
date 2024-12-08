import json
import os
from typing import Literal

import google.generativeai as genai  # type: ignore
import i18n  # type: ignore
import typing_extensions as typing


class GameResponse(typing.TypedDict):
    questText: str
    responseVariants: list[str]
    mood: Literal['neutral', 'curious', 'fear', 'happy']


i18n.load_path.append('src/locales')
i18n.set('locale', os.environ['LOCALE'])

class GeminiChatbot:
    def __init__(self):
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        self.model = genai.GenerativeModel(
            os.environ['GEMINI_VERSION'],
            generation_config=genai.GenerationConfig(
                response_mime_type='application/json',
                response_schema=GameResponse
            )
        )
        self.chat = self.model.start_chat(history=[])
        self.chat.send_message(i18n.t('game.init_game'))

    def send_message(self, message):
        response = self.chat.send_message(message)
        return json.loads(response.text)