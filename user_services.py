from db import test_connection
from security import hash_password, verify_password
from mysql.connector import Error

def create_user(name: str, email: str, password: str, role: str) -> bool:
    conn = test_connection()
    if conn is None:
        print(" Failed to connect to database")
        return False

    cursor = conn.cursor()
    try:
        print("Inserting:", name, email, hash_password(password), role)
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
            (name, email, hash_password(password), role)
        )
        conn.commit()
        print(" User inserted successfully")
        return True
    except Error as e:
        print(f" Database error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


def authenticate_user(email: str, password: str):
    """Validate user credentials."""
    conn = test_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        if user and verify_password(password, user["password"]):
            return user
        return None
    finally:
        cursor.close()
        conn.close()



def get_user_id(email: str):
    conn = test_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
        result = cursor.fetchone()
        if result:
            return result[0]  # ID is the first column
        return None
    finally:
        cursor.close()
        conn.close()
