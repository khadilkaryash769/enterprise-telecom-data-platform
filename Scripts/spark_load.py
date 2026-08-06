import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def load_data(df):

    jdbc_url = (
        f"jdbc:postgresql://"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    (
        df.write
        .format("jdbc")
        .option("url", jdbc_url)
        .option("dbtable", "customers_spark")
        .option("user", os.getenv("DB_USER"))
        .option("password", os.getenv("DB_PASSWORD"))
        .option("driver", "org.postgresql.Driver")
        .mode("overwrite")
        .save()
    )

    print("Data Loaded Successfully into PostgreSQL")