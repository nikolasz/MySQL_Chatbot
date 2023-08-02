# database.py
import mysql.connector

def create_connection():
    """
    Create a connection to the database.

    Returns:
        obj: The connection object.
    """
    config = {
        'user': '<your-database-user>',
        'password': '<your-database-password>',
        'host': '<your-database-host>',
        'database': '<your-database>',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)

    return cnx


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
