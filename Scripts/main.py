import logging

from extract import extract_customers
from transform import transform_customers
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
# Load
# -------------------------------
print("Step 3 : Loading data into PostgreSQL...")
load_customers(df)
print("Loading Completed")

logging.info("ETL Pipeline Finished")

print("========== ETL PIPELINE FINISHED ==========")