# query_services.py
from db import test_connection
import pandas as pd
from datetime import datetime
from mysql.connector import Error

def add_query(user_id: int, email:str,heading: str, description: str, mobile: str = None) -> bool:
 
    try:
        conn = test_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO queries (user_id, email, heading, description, mobile) VALUES (%s, %s, %s, %s, %s)",
            (user_id, email, heading, description, mobile)
        )

        conn.commit()

        print(" Query inserted successfully!")
        return True

    except Error as e:
        print(f"Database error while inserting query: {e}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_all_queries():
    conn = test_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT q.id, u.name AS client_name, u.email, q.heading, q.description, q.status, q.query_created_time,q.query_closed_time
        FROM queries q
        JOIN users u ON q.user_id = u.id
        ORDER BY q.query_created_time DESC;
    """)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


def update_queries(edited_df: pd.DataFrame):
    """
    Update edited queries back into MySQL.
    """
    conn = test_connection()
    cursor = conn.cursor()

    try:
        for _, row in edited_df.iterrows():
            query_id = row["id"]
            description = row["description"]
            status = row["status"]
            print(status)

            # If query is closed → set closed_time
            closed_time = None
            if status == "Closed":
                closed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("""
                UPDATE queries
                SET description = %s,
                    status = %s,
                    query_closed_time = %s
                WHERE id = %s
            """, (description, status, closed_time, query_id))
        
        conn.commit()
        return True
    except Exception as e:
        print("Database update failed:", e)
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()


def get_user_queries(email: str):
    """
    Fetch all queries for the logged-in user.
    """
    conn = test_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT 
                id AS query_id,
                heading,
                description,
                status,
                query_created_time,
                query_closed_time
            FROM queries
            WHERE email = %s
            ORDER BY query_created_time DESC
        """, (email,))
        
        data = cursor.fetchall()
        return data
    except Exception as e:
        print("Failed to fetch user queries:", e)
        return []
    finally:
        cursor.close()
        conn.close()
