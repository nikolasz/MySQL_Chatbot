# database.py
# import mysql.connector commented out for now
from config import get_db_config

def get_mysql_schema(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT table_name, column_name, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema = DATABASE()")
    schema = {}
    for table_name, column_name, data_type in cursor:
        if table_name not in schema:
            schema[table_name] = {}
        schema[table_name][column_name] = data_type
    return schema


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
    '''
    Execute a query on the database.

    Args:
        cnx (obj): The database connection object.
        query (str): The SQL query to execute.
        params (tuple, optional): The parameters for the SQL query.

    Returns:
        list: The result of the query.
    '''
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
