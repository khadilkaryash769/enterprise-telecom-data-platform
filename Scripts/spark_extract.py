from pyspark.sql import SparkSession


def extract_data(spark):
    df = spark.read.csv(
        "data/Raw/customers.csv",
        header=True,
        inferSchema=True
    )
    return df