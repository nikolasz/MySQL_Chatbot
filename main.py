# main.py
import os
import sys
import json
sys.path.insert(0, os.path.abspath('modules'))

from modules.config import load_config
from modules.schema import load_schema
from modules.openai_api import init_openai_api
from modules.query_generator import generate_sql_query
from modules.database import create_connection, execute_query, close_connection
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
    try:
        schema_path = os.path.join(current_directory, 'schema.json')
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        print(f'Schema loaded: {json.dumps(schema, indent=4)}')
    except FileNotFoundError:
        logging.error(f"Schema file {schema_path} does not exist.")
        schema = None
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        schema = None
        
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
