from spark_logger import logger

def extract_data(spark):

    file_path = "data/Raw/customers.csv"

    logger.info(f"Reading file : {file_path}")

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(file_path)
    )

    print(f"Extracted Records : {df.count()}")

    logging.info(f"Extracted {df.count()} records")

    return df