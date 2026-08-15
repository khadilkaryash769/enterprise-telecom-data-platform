# Databricks / PySpark
# Source: Databricks notebook screenshots

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

print("Spark version:", spark.version)

s3_path = "s3://enterprise-telecom-data-yash-2026/customers.csv"
print(s3_path)

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(s3_path)
)

print("Records:", df.count())
display(df.limit(10))
