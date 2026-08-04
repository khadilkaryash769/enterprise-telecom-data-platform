from pyspark.sql import SparkSession

from spark_extract import extract_data
from spark_transform import transform_data
from spark_validate import validate_customers
from spark_load import load_data


def main():

    spark = (
        SparkSession.builder
        .appName("Enterprise Telecom Data Platform")
        .master("local[*]")
        .config(
            "spark.jars",
            r"C:\Project\enterprise-telecom-data-platform\jars\postgresql-42.7.12.jar"
        )
        .getOrCreate()
    )

    print("=" * 50)
    print("Spark Session Created Successfully!")
    print("Spark Version :", spark.version)
    print("=" * 50)

    # -----------------------------
    # Extract
    # -----------------------------
    print("Step 1 : Extracting Data...")

    df = extract_data(spark)

    print(f"Total Records : {df.count()}")

    # -----------------------------
    # Transform
    # -----------------------------
    print("Step 2 : Transforming Data...")

    df = transform_data(df)

    print("Transformation Completed")

    # -----------------------------
    # Validation
    # -----------------------------
    print("Step 3 : Validating Data...")

    valid_df, invalid_df = validate_customers(df)

    print(f"Valid Records   : {valid_df.count()}")
    print(f"Invalid Records : {invalid_df.count()}")

    # -----------------------------
    # Load
    # -----------------------------
    print("Step 4 : Loading Data...")

    load_data(valid_df)

    print("Loading Completed")

    spark.stop()

    print("=" * 50)
    print("Spark ETL Pipeline Finished Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()