# query_generator.py
from openai_api import generate_response
import json
import logging

def generate_sql_query(schema, query, sql_commands):
    # Prepare the system message
    system_message = f'''
    You are an SQL query generator. Generate an SQL query based on the following schema, SQL commands, and user's input.
    Schema: {json.dumps(schema, indent=4)}
    SQL Commands: {json.dumps(sql_commands, indent=4)}
    '''

    # Prepare the messages
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": query}
    ]
    # Print schema and SQL commands for debugging
    print(f'Schema: {json.dumps(schema, indent=4)}')
    print(f'SQL Commands: {json.dumps(sql_commands, indent=4)}')
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
