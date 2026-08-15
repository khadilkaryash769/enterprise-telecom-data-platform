from incremental_extract import incremental_extract


df = incremental_extract(
    "data/raw/customers.csv"
)


print(df.head())
print("Records:", len(df))