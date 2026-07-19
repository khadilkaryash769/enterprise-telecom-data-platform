import logging
import os
import io

import psycopg
from dotenv import load_dotenv

load_dotenv()


def load_customers(df):

    conn = None
    cur = None

    try:

        print("Connecting to PostgreSQL...")

        conn = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        print("Connected Successfully!")

        cur = conn.cursor()

        # Table clean
        cur.execute(
            "TRUNCATE TABLE customers RESTART IDENTITY"
        )

        print("Table Truncated")


        # DataFrame ko CSV memory buffer me convert karo
        buffer = io.StringIO()

        df.to_csv(
            buffer,
            index=False,
            header=False
        )

        buffer.seek(0)


        # PostgreSQL COPY
        cur.copy(
            """
            COPY customers
            (
                customer_id,
                first_name,
                last_name,
                phone_number,
                email,
                city,
                plan_type
            )
            FROM STDIN
            WITH CSV
            """,
            buffer
        )


        conn.commit()


        logging.info(
            f"Loaded {len(df)} customers using COPY"
        )

        print(
            f"✅ Loaded {len(df)} customers using COPY"
        )


    except Exception as e:

        logging.exception(
            "COPY Load Failed"
        )

        print(
            "❌ ERROR:",
            e
        )


    finally:

        if cur:
            cur.close()

        if conn:
            conn.close()

        print(
            "Database Connection Closed"
        )