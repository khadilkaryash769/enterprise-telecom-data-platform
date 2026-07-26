from pyspark.sql import SparkSession
from spark_extract import extract_data


def main():

    spark = (
        SparkSession.builder
        .appName("Enterprise Telecom Data Platform")
        .master("local[*]")
        .getOrCreate()
    )

    print("=" * 50)
    print("Spark Session Created Successfully!")
    print(f"Spark Version : {spark.version}")
    print("=" * 50)

    df = extract_data(spark)

    print("\nFirst 5 Records")
    df.show(5)

    print("\nSchema")
    df.printSchema()

    spark.stop()


if __name__ == "__main__":
    main()