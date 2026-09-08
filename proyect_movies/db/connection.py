import mysql.connector
from mysql.connector import connection
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env" # Search my current file
load_dotenv(dotenv_path=env_path) # The values ​​from the .env file can be used


def get_connection():
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD") 
    DB_DATABASE = os.getenv("DB_DATABASE")

    my_db = {  
        'host': DB_HOST,
        'user': DB_USER,
        'password': DB_PASSWORD,
        'database':DB_DATABASE
        }   
        
    conn = None

    try:
        conn = connection.MySQLConnection(**my_db) # It will establish the connection with key-values pairs

    except mysql.connector.Error as error:
        print("Database Error:", error) 
    return conn