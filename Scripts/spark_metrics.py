from datetime import datetime


def print_metrics(total_records, valid_records, invalid_records):

    print("\n" + "=" * 60)
    print("              ETL EXECUTION REPORT")
    print("=" * 60)

    print(f"Execution Time : {datetime.now()}")
    print(f"Total Records  : {total_records}")
    print(f"Valid Records  : {valid_records}")
    print(f"Invalid Records: {invalid_records}")
    print(f"Success Rate   : {(valid_records / total_records) * 100:.2f}%")

    print("=" * 60)