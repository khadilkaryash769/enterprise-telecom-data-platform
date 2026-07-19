import os
import logging
from datetime import datetime


def save_bad_records(df):

    if df.empty:
        logging.info("No bad records found")
        print("No invalid records to save")
        return

    folder = "data/bad_records"

    os.makedirs(folder, exist_ok=True)

    file_name = f"invalid_customers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    file_path = os.path.join(folder, file_name)

    df.to_csv(file_path, index=False)

    logging.info(f"Saved bad records: {file_path}")

    print(f"⚠️ Invalid records saved: {file_path}")