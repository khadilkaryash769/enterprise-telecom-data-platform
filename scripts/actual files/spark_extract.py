from spark_logger import logger
from spark_metadata import get_last_loaded_id
from pyspark.sql.functions import col


def extract_data(spark):

    file_path = "data/Raw/customers.csv"

    logger.info(f"Reading file : {file_path}")

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(file_path)
    )

    print(f"Total Records Found : {df.count()}")

    # Read last loaded id from metadata table
    last_loaded_id = get_last_loaded_id()

    print(f"Last Loaded ID : {last_loaded_id}")

    # Incremental Filter
    df = df.filter(
        col("customer_id") > last_loaded_id
    )

    print(f"New Records Found : {df.count()}")

    logger.info(f"New Records : {df.count()}")

    return df