# main.py
from config import load_config
from schema import load_schema
from openai_api import init_openai_api
from query_generator import generate_mysql_query
from database import create_connection, execute_query, close_connection
import logging

def main():
    # Set up logging
    logging.basicConfig(filename='app.log', level=logging.INFO)

    # Load config and schema.
    config = load_config()
    schema_file = "schema.json"  # This could be an input or configuration
    schema = load_schema(schema_file)

    # Generate SQL query.
    query = input("Enter a natural language prompt: ")

    cnx = None
    try:
        sql_query = generate_mysql_query(schema, query)
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
