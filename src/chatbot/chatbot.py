import json
import os

import google.generativeai as genai
import i18n
from dotenv import load_dotenv

from src.utils.helpers import remove_markdown

load_dotenv()
i18n.load_path.append('src/locales')
i18n.set('locale', 'ru')

class GeminiChatbot:
    def __init__(self):
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        self.model = genai.GenerativeModel(os.environ['GEMINI_VERSION'])
        self.chat = self.model.start_chat(history=[])
        self.chat.send_message(i18n.t('game.init_game'))

    def send_message(self, message):
        response = self.chat.send_message(message)
        return json.loads(str(remove_markdown(response.text, 'json')))