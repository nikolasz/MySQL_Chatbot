# database.py
import mysql.connector
from config import get_db_config

def create_connection():
    db_config = get_db_config()
    try:
        cnx = mysql.connector.connect(user=db_config['user'], password=db_config['password'], host=db_config['host'], database=db_config['database'])
        if cnx.is_connected():
            print("Successfully connected to the database.")
            return cnx
    except Error as e:
        print(f"The error '{e}' occurred.")

def execute_query(cnx, query, params=None):
    """
    Execute a query on the database.

    Args:
        cnx (obj): The database connection object.
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters for the SQL query.

    Returns:
        list: The result of the query.
    """
    cursor = cnx.cursor()
    cursor.execute(query, params)

    result = cursor.fetchall()

    cursor.close()

    return result


def close_connection(cnx):
    """
    Close the connection to the database.

    Args:
        cnx (obj): The database connection object.
    """
    cnx.close()
