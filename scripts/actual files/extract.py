import pandas as pd
import logging
import os

import psycopg
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

def get_last_loaded_id():

    conn = None
    cur = None

    try:
        print("USER:", os.getenv("DB_USER"))
        print("PASSWORD:", os.getenv("DB_PASSWORD"))
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
            WHERE table_name = 'customers'
        """)

        result = cur.fetchone()

        return result[0] if result else 0

    finally:
        if cur:
            cur.close()

        if conn:
            conn.close()


def extract_customers(file_path):

    logging.info(f"Reading file: {file_path}")

    df = pd.read_csv(file_path)

    logging.info(f"Read {len(df)} records")

    last_loaded_id = get_last_loaded_id()

    print(f"Last Loaded ID : {last_loaded_id}")

    df = df[
        df["customer_id"] > last_loaded_id
    ]

    print(f"New Records Found : {len(df)}")

    logging.info(
        f"New Records Found : {len(df)}"
    )

    return df