# query_generator.py
from openai_api import generate_response
import json
import logging
from schema import load_schema
import os

# Load SQL arguments

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the path to sql_commands.json
sql_commands_path = os.path.join(current_directory, 'sql_commands.json')

# Load SQL arguments
with open(sql_commands_path) as f:
    sql_commands = json.load(f)

with open('schema.json') as f:
    schema_file = 'schema.json'
    schema = load_schema(os.path.join(current_directory, schema_file))
    
def generate_sql_query(schema, query, sql_commands):
    # Prepare the system message
    system_message = f'''
    You are an SQL query generator. Generate an SQL query based on the following schema, SQL commands and user's input.
    Schema: {json.dumps(schema, indent=4)}
    SQL Commands: {json.dumps(sql_commands, indent=4)}
    '''
    # Print schema and SQL commands for debugging
    print(f'Schema: {json.dumps(schema, indent=4)}')
    print(f'SQL Commands: {json.dumps(sql_commands, indent=4)}')
    # Prepare the messages
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": query}
    ]

    # Call OpenAI API
    response = generate_response(messages)

    # Error checking
    if not response:
        logging.error(f"No response received for query: {query}")
        return 'error'
    if 'error' in response:
        logging.error(f"An error occurred while generating the query: {response}")
        return 'error'

    # Return the generated SQL query
    return response

def generate_mysql_query(schema, query):
    return generate_sql_query(schema, query)
