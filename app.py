from flask import Flask
from dotenv import load_dotenv
import google.generativeai as genai
import os

app = Flask(__name__)

load_dotenv()
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

@app.get('/chatbot')
def get_chatbot():
    flash = genai.GenerativeModel('gemini-1.5-flash')
    response = flash.generate_content("Write very short introductory funny welcome sentence")
    return response.text
