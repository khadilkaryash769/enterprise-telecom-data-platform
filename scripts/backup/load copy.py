import os
import psycopg

def load_customers(df):
    print("Current working directory:", os.getcwd())

    conn = psycopg.connect(
        host="127.0.0.1",
        port=5432,
        dbname="telecom_db",
        user="admin",
        password="admin123",
        connect_timeout=5
    )

    print("Connected Successfully!")

    conn.close()