import mysql.connector
from mysql.connector import Error

def test_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",       # Hostname from Workbench
            port=3306,              # Default MySQL port
            user="root",            # Your Workbench username
            password="root",# Replace with your MySQL password
            database="query_portal" # Database name you created
        )

        if connection.is_connected():
            print("Successfully connected to MySQL database!")
            # db_info = connection.get_server_info()
            # print("MySQL Server version:", db_info)

    except Error as e:
        print(" Error while connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            return connection
            print("MySQL connection is closed.")

test_connection()
