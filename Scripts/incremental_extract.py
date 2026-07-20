import logging
import pandas as pd
import psycopg
import os

from dotenv import load_dotenv

load_dotenv()


def get_last_loaded_id():

    conn = None
    cur = None

    try:

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

        return result[0]

    finally:

        if cur:
            cur.close()

        if conn:
            conn.close()



def incremental_extract(file_path):

    logging.info("Incremental Extract Started")


    last_id = get_last_loaded_id()

    print(f"Last Loaded ID: {last_id}")


    df = pd.read_csv(file_path)


    new_df = df[
        df["customer_id"] > last_id
    ]


    logging.info(
        f"New records found: {len(new_df)}"
    )


    return new_df