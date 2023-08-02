# query_generator.py
from openai_api import generate_response
import json

def generate_sql_query(schema, query, command):
    system_message = f'''
    You are an SQL query generator. Generate a {command.upper()} query based on the following schema and user's input.
    Schema: ''' + json.dumps(schema, indent=4)

    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": query}
    ]

    return generate_response(messages)

def generate_mysql_query(schema, query, command):
    if command.lower() in ['select', 'insert', 'update', 'delete']:
        return generate_sql_query(schema, query, command)
    else:
        return 'error'