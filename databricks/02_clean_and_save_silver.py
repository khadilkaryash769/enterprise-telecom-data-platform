# Databricks / PySpark
# Source: Databricks notebook screenshots

from pyspark.sql import functions as F
from pyspark.sql.functions import col, trim, lower

# Input table created in Unity Catalog
silver_df = (
    spark.table("enterprise_telecom_customers")
    .dropDuplicates()
    .dropna(subset=["customer_id"])
)

# Clean string columns
for column in silver_df.columns:
    if dict(silver_df.dtypes)[column] == "string":
        silver_df = silver_df.withColumn(
            column,
            trim(col(column))
        )

# Standardize email
if "email" in silver_df.columns:
    silver_df = silver_df.withColumn(
        "email",
        lower(col("email"))
    )

print("Silver Records:", silver_df.count())
display(silver_df.limit(10))

silver_path = "/Volumes/workspace/default/enterprise_telecom_vol/silver/customers"

(
    silver_df.write
    .format("delta")
    .mode("overwrite")
    .save(silver_path)
)

print("Silver Delta data saved successfully!")
