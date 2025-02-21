import os
from typing import Literal, List

import i18n

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

from pydantic import BaseModel


class GameResponse(BaseModel):
    questText: str
    responseVariants: List[str]
    mood: Literal['neutral', 'curious', 'fear', 'happy']


i18n.load_path.append('src/locales')
i18n.set('locale', os.environ['LOCALE'])

class Chatbot:
    def __init__(self):
        model = GoogleGenerativeAI(
            model=os.environ['LLM_VERSION'],
            temperature=os.environ['LLM_TEMPERATURE'],
        )
        parser = JsonOutputParser(pydantic_object=GameResponse)
        prompt = PromptTemplate(
            template=i18n.t('game.init_game') + "\n{answer}\n{format_instructions}\n",
            input_variables=['answer'],
            partial_variables={'format_instructions': parser.get_format_instructions()},
        )
        self.chain = prompt | model | parser

    def send_message(self, message):
        return self.chain.invoke(message)
