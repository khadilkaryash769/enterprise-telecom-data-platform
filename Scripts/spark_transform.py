from pyspark.sql.functions import col, trim


def transform_data(df):

    print("Rows before cleaning:", df.count())

    # Remove duplicate rows
    df = df.dropDuplicates()

    # Remove rows with NULL customer_id
    df = df.dropna(subset=["customer_id"])

    # Trim string columns
    for column in df.columns:
        if dict(df.dtypes)[column] == "string":
            df = df.withColumn(column, trim(col(column)))

    print("Rows after cleaning:", df.count())

    return df