import json
import os
from typing import Literal

import i18n  # type: ignore
import typing_extensions as typing

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage


class GameResponse(typing.TypedDict):
    questText: str
    responseVariants: list[str]
    mood: Literal['neutral', 'curious', 'fear', 'happy']


i18n.load_path.append('src/locales')
i18n.set('locale', os.environ['LOCALE'])

class Chatbot:
    def __init__(self):
        self.model = GoogleGenerativeAI(
            model=os.environ['LLM_VERSION'],
            temperature=os.environ['LLM_TEMPERATURE'],
            )
        self.model.invoke([SystemMessage(i18n.t('game.init_game'))])

    def send_message(self, message):
        return self.model.invoke(message)
