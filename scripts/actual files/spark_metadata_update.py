import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def update_last_loaded_id(last_loaded_id):

    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute(
        """
        UPDATE etl_metadata
        SET last_loaded_id = %s
        WHERE table_name = 'customers'
        """,
        (last_loaded_id,)
    )

    conn.commit()

    cur.close()
    conn.close()