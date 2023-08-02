# main.py
from config import load_config
from schema import load_schema
from openai_api import init_openai_api, send_message
from query_generator import generate_mysql_query
from schema import load_schema_from_file
from query_generator import generate_mysql_query
from database import create_connection, execute_query, close_connection
import openai_api

schema = load_schema('path/to/schema.json')

def main():
    # Load config and schema.
    config = load_config()
    schema = load_schema_from_file("schema.json")

    # Initialize OpenAI API.
    init_openai_api(config['OPENAI_API_KEY'])

    # Generate SQL query.
    query = input("Enter a natural language prompt: ")
    sql_query = generate_mysql_query(schema, query)

    print(sql_query)

    cnx = create_connection()
    result = execute_query(cnx, sql_query)
    close_connection(cnx)
    print(result)

if __name__ == '__main__':
    main()
