# Databricks / PySpark
# Source: Databricks notebook screenshots

from pyspark.sql.functions import count

gold_df = (
    silver_df
    .groupBy("plan_type")
    .agg(
        count("*").alias("customer_count")
    )
    .orderBy("plan_type")
)

display(gold_df)
