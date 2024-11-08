import psycopg2
from psycopg2 import Error

def connect_to_db(username, password, host, port, database):
    try:
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()
        print("Connected to the database")
        return cursor, connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None, None

def disconnect_from_db(connection, cursor):
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
        print("Connection does not exist.")

def run_and_fetch_sql(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        if cursor.description:
            record = cursor.fetchall()
            return record
        return []
    except (Exception, Error) as error:
        print("Errors while executing the code: ", error)
        return -1

