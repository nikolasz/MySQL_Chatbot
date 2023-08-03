import os
import sys
import json
sys.path.insert(0, os.path.abspath('modules'))

from config import load_config
from schema import load_schema
from openai_api import init_openai_api
from query_generator import generate_sql_query
from database import create_connection, execute_query, close_connection
import logging

def main():
    # Set up logging
    logging.basicConfig(filename='app.log', level=logging.INFO)

    # Load config and schema.
    config = load_config()
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Load SQL commands
    sql_commands_path = os.path.join(current_directory, 'sql_commands.json')
    with open(sql_commands_path, 'r') as f:
        sql_commands = json.load(f)

    # Load schema
    schema = load_schema(os.path.join(current_directory, 'modules', 'schema.json'))

    # Generate SQL query.
    query = input("Enter a natural language prompt: ")

    cnx = None

    try:
        sql_query = generate_sql_query(schema, query, sql_commands)
        print(sql_query)

        cnx = create_connection()
        result = execute_query(cnx, sql_query)
        print(result)

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

    finally:
        if cnx:
            close_connection(cnx)

if __name__ == '__main__':
    main()
