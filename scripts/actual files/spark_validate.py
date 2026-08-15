from pyspark.sql.functions import col, count
from pyspark.sql.window import Window


def validate_customers(df):

    # Duplicate Phone Number Check
    window_spec = Window.partitionBy("phone_number")

    df = df.withColumn(
        "phone_count",
        count("phone_number").over(window_spec)
    )

    # Invalid Records
    invalid_df = df.filter(
        (col("phone_number").isNull()) |
        (col("first_name").isNull()) |
        (col("last_name").isNull()) |
        (col("email").isNull()) |
        (~col("email").contains("@")) |
        (~col("plan_type").isin("PREPAID", "POSTPAID")) |
        (col("phone_count") > 1)
    )

    # Valid Records
    valid_df = df.subtract(invalid_df)

    # Remove Helper Column
    valid_df = valid_df.drop("phone_count")
    invalid_df = invalid_df.drop("phone_count")

    return valid_df, invalid_df