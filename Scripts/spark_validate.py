from pyspark.sql.functions import col


def validate_customers(df):

    valid_df = df.filter(
        col("phone_number").isNotNull()
    )

    invalid_df = df.filter(
        col("phone_number").isNull()
    )

    return valid_df, invalid_df