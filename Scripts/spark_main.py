from pyspark.sql import SparkSession
from spark_extract import extract_data
from spark_transform import transform_data
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

    df = extract_data(spark)
    df = transform_data(df)

    load_data(df)

    spark.stop()

if __name__ == "__main__":
    main()