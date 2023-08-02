# openai_api.py
import openai
from config import get_openai_api_key

def init_openai_api():
    openai.api_key = get_openai_api_key()

def generate_response(messages):
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.1,
        max_tokens=200
    )

    return response['choices'][0]['message']['content'].strip()
