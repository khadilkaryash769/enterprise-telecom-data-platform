from pyspark.sql import SparkSession

from spark_extract import extract_data
from spark_transform import transform_data
from spark_validate import validate_customers
from spark_load import load_data
from spark_metrics import print_metrics


def main():

    spark = (
        SparkSession.builder
        .appName("Enterprise Telecom Data Platform")
        .master("local[*]")
        .config(
            "spark.jars",
            r"C:\Project\enterprise-telecom-data-platform\jars\postgresql-42.7.12.jar"
        )
        .config("spark.driver.extraJavaOptions", "-Duser.timezone=UTC")
        .getOrCreate()
    )

    print("=" * 50)
    print("Spark Session Created Successfully!")
    print(f"Spark Version : {spark.version}")
    print("=" * 50)

    # Step 1
    print("Step 1 : Extracting Data...")
    df = extract_data(spark)

    # Step 2
    print("Step 2 : Transforming Data...")
    df = transform_data(df)
    print("Transformation Completed")

    # Step 3
    print("Step 3 : Validating Data...")
    valid_df, invalid_df = validate_customers(df)

    print(f"Valid Records   : {valid_df.count()}")
    print(f"Invalid Records : {invalid_df.count()}")

    # Step 4
    print("Step 4 : Loading Data...")
    load_data(valid_df)

    print("Loading Completed")
    
    print_metrics(
    total_records=df.count(),
    valid_records=valid_df.count(),
    invalid_records=invalid_df.count()
)

    # Summary
    print("\n" + "=" * 50)
    print("ETL SUMMARY")
    print("=" * 50)
    print(f"Total Records   : {df.count()}")
    print(f"Valid Records   : {valid_df.count()}")
    print(f"Invalid Records : {invalid_df.count()}")
    print(f"Loaded Records  : {valid_df.count()}")
    print("=" * 50)

    spark.stop()

    print("Spark ETL Pipeline Finished Successfully!")


if __name__ == "__main__":
    main()