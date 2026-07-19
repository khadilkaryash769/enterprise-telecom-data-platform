import logging

from config_loader import load_config
config = load_config()
print(config)

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

df = extract_customers("data/raw/customers.csv")

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

total_records = len(df)
valid_records = len(valid_df)
invalid_records = len(bad_df)

print(f"Valid Records: {valid_records}")
print(f"Invalid Records: {invalid_records}")


# -------------------------------
# Save Bad Records
# -------------------------------
save_bad_records(bad_df)


# -------------------------------
# Load
# -------------------------------
print("Step 4 : Loading data into PostgreSQL...")

load_customers(valid_df)

print("Loading Completed")


# -------------------------------
# ETL Summary
# -------------------------------
print("\n========== ETL SUMMARY ==========")

print(f"Total Records    : {total_records}")
print(f"Valid Records    : {valid_records}")
print(f"Invalid Records  : {invalid_records}")
print(f"Loaded Records   : {valid_records}")

print("ETL Status       : SUCCESS")

print("=================================")


logging.info("ETL Pipeline Finished")


print("========== ETL PIPELINE FINISHED ==========")