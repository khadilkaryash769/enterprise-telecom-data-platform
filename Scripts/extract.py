import pandas as pd
import logging

def extract_customers(file_path):
    logging.info(f"Reading file: {file_path}")

    df = pd.read_csv(file_path)

    logging.info(f"Read {len(df)} records")

    return df