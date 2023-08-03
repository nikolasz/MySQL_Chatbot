import os
from dotenv import load_dotenv

load_dotenv()
def load_config():
    config = {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'DB_USER': os.getenv('DB_USER'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD'),
        'DB_HOST': os.getenv('DB_HOST'),
        'DB_DATABASE': os.getenv('DB_DATABASE')
    }
    return config

def get_openai_api_key():
    return load_config()['OPENAI_API_KEY']

def get_db_config():
    config = load_config()
    return {
        'user': config['DB_USER'],
        'password': config['DB_PASSWORD'],
        'host': config['DB_HOST'],
        'database': config['DB_DATABASE']
    }