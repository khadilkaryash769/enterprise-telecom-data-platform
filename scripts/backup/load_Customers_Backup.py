import logging
import os

import pandas as pd
import psycopg
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("HOST =", os.getenv("DB_HOST"))
print("PORT =", os.getenv("DB_PORT"))
print("DB =", os.getenv("DB_NAME"))
print("USER =", os.getenv("DB_USER"))
print("PASSWORD =", os.getenv("DB_PASSWORD"))

# Configure logging
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

conn = None
cur = None

try:
    logging.info("ETL Started")

    # Read CSV
    df = pd.read_csv("data/raw/customers.csv")
    logging.info(f"CSV loaded successfully. Rows: {len(df)}")

    # Connect to PostgreSQL
    conn = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    logging.info("Connected to PostgreSQL")

    cur = conn.cursor()

    # Clean table
    cur.execute("TRUNCATE TABLE customers RESTART IDENTITY")

    # Prepare records for bulk insert
    records = [
        (
            int(row["customer_id"]),
            row["first_name"],
            row["last_name"],
            str(row["phone_number"]),
            row["email"],
            row["city"],
            row["plan_type"]
        )
        for _, row in df.iterrows()
    ]

    logging.info(f"Prepared {len(records)} records for bulk insert")

    # Bulk insert
    cur.executemany(
        """
        INSERT INTO customers
        (customer_id, first_name, last_name, phone_number, email, city, plan_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        records
    )

    conn.commit()

    logging.info("Bulk insert completed")
    logging.info(f"Loaded {len(df)} customers into PostgreSQL")

    print(f"✅ Loaded {len(df)} customers into PostgreSQL.")

except Exception as e:
    logging.error(f"ETL Failed: {e}")
    print(f"❌ Error: {e}")

finally:
    if cur:
        cur.close()

    if conn:
        conn.close()

    logging.info("Database connection closed")
    logging.info("ETL Finished")