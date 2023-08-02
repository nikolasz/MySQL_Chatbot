# main.py
from config import load_config
from schema import load_schema
from openai_api import init_openai_api
from query_generator import generate_mysql_query
from database import create_connection, execute_query, close_connection

def main():
    # Load config and schema.
    config = load_config()
    schema = load_schema("schema.json")

    # Generate SQL query.
    query = input("Enter a natural language prompt: ")
    sql_query = generate_mysql_query(schema, query)

    print(sql_query)

    cnx = None
    try:
        cnx = create_connection()
        result = execute_query(cnx, sql_query)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cnx:
            close_connection(cnx)

if __name__ == '__main__':
    main()
