import logging

from extract import extract_customers
from transform import transform_customers
from validate import validate_customers
from save_bad_records import save_bad_records
from load import load_customers


logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


print("========== ETL PIPELINE STARTED ==========")

logging.info("ETL Pipeline Started")


# -------------------------------
# Extract
# -------------------------------
print("Step 1 : Extracting data...")

df = extract_customers(
    "data/raw/customers_incremental.csv"
)

print(f"Extracted {len(df)} rows")


# -------------------------------
# Transform
# -------------------------------
print("Step 2 : Transforming data...")

df = transform_customers(df)

print("Transformation Completed")


# -------------------------------
# Validation
# -------------------------------
print("Step 3 : Validation Started")

valid_df, bad_df = validate_customers(df)

print(f"Valid Records : {len(valid_df)}")
print(f"Invalid Records : {len(bad_df)}")


# -------------------------------
# Save Bad Records
# -------------------------------
if len(bad_df) > 0:
    save_bad_records(bad_df)
else:
    print("No invalid records to save")


# -------------------------------
# Load
# -------------------------------
print("Step 4 : Loading data into PostgreSQL...")

if len(valid_df) > 0:
    load_customers(valid_df)
else:
    print("No new records to load")


# -------------------------------
# Summary
# -------------------------------
print("\n========== ETL SUMMARY ==========")

print(f"Total Records   : {len(df)}")
print(f"Valid Records   : {len(valid_df)}")
print(f"Invalid Records : {len(bad_df)}")

print("ETL Status      : SUCCESS")

print("=================================")


logging.info("ETL Pipeline Finished")


print("========== ETL PIPELINE FINISHED ==========")