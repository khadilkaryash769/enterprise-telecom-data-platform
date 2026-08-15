# Databricks / PySpark
# Source: Databricks notebook screenshots

# Read the Delta files from the volume
delta_path = "/Volumes/workspace/default/enterprise_telecom_vol/customers"

df_from_delta = (
    spark.read
    .format("delta")
    .load(delta_path)
)

df_from_delta.write     .format("delta")     .mode("overwrite")     .saveAsTable("enterprise_telecom_customers")

print("Table Registered Successfully!")
