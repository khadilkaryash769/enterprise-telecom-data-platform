def load_data(df):
    (
        df.write
        .format("jdbc")
        .option("url", "jdbc:postgresql://127.0.0.1:5432/telecom_db")
        .option("dbtable", "customers_spark")
        .option("user", "admin")
        .option("password", "admin123")
        .option("driver", "org.postgresql.Driver")
        .mode("overwrite")
        .save()
    )

    print("Data Loaded Successfully into PostgreSQL")