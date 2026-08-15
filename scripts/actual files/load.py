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


        # ---------------------------------
        # Prepare Data for COPY
        # ---------------------------------

        buffer = io.StringIO()

        df.to_csv(
            buffer,
            index=False,
            header=False
        )

        buffer.seek(0)


        # ---------------------------------
        # Incremental Insert
        # ---------------------------------

        with cur.copy(
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
            """
        ) as copy:

            copy.write(buffer.getvalue())


        conn.commit()


        print(
            f"✅ Loaded {len(df)} new customers"
        )


        logging.info(
            f"Loaded {len(df)} new customers"
        )


        # ---------------------------------
        # Update Metadata
        # ---------------------------------

        last_customer_id = int(
            df["customer_id"].max()
        )


        cur.execute(
            """
            UPDATE etl_metadata
            SET last_loaded_id = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE table_name = 'customers'
            """,
            (last_customer_id,)
        )


        conn.commit()


        print(
            f"Metadata Updated. Last Loaded ID = {last_customer_id}"
        )


    except Exception as e:

        logging.exception(
            "Incremental Load Failed"
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