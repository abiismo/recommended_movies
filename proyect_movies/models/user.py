import bcrypt
import mysql.connector
import sys
import os

try:     
    from db import connection # Import the function that does the connection
except ImportError:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if root not in sys.path:
        sys.path.insert(0, root)
    from db import connection
         
def register(user_name: str, user_password: str):
    """Hash a password for storage during registration
         
    Args:
        user (str): name of the user
        hash_password (str): password of the user
    """  
         
    bytePwd = user_password.encode('utf-8') # Converting text data into a specific character set
    mySalt = bcrypt.gensalt(rounds=12) # embeds a unique random salt -> In this case have a "salt" of 12
         
    # Hash password
    pwd_hash = bcrypt.hashpw(bytePwd, mySalt)
         
         
    try: 
        conn = connection.get_connection() # -> Does the connection with this funcion
         
        if conn is None: return None 
         
        cursor = conn.cursor()
         
        query = """
        INSERT INTO user (name_user, password_user)
        VALUES (%s, %s)
        """
         
        values = (user_name, pwd_hash)
        cursor.execute(query, values)
        conn.commit()
         
    except mysql.connector.Error as error:
        print(f"Data base error: {error}")
        conn.rollback()
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def login(user_name: str, user_password: str) -> bool: # if is correct, should return True
    """Verify an entered password against the stored hash."""
    try:
        conn = connection.get_connection()

        if conn is None: return None

        cursor = conn.cursor()

        select_sql = """
        SELECT password_user FROM user WHERE name_user = %s
        """

        cursor.execute(select_sql, (user_name,))
        account = cursor.fetchone()

        if not account:
            return False
        
        bytePwd = user_password.encode('utf-8')

        account_bytes = account[0].encode('utf-8')

        check = bcrypt.checkpw(bytePwd, account_bytes)

        if check: 
            return True
        return False

    except mysql.connector.Error as error:
        print(f'Data base connection error: {error}')
        conn.rollback()
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


