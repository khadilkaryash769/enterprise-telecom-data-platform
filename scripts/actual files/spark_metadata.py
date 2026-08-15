import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def get_last_loaded_id():

    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT last_loaded_id
        FROM etl_metadata
        WHERE table_name='customers'
    """)

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result[0] if result else 0