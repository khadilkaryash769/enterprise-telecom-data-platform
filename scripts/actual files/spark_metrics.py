from datetime import datetime


def print_metrics(total_records, valid_records, invalid_records):

    print("\n")
    print("=" * 70)
    print("ETL EXECUTION REPORT")
    print("=" * 70)

    print(f"Execution Time : {datetime.now()}")
    print(f"Total Records  : {total_records}")
    print(f"Valid Records  : {valid_records}")
    print(f"Invalid Records: {invalid_records}")

    if total_records == 0:
        success_rate = 0
    else:
        success_rate = (valid_records / total_records) * 100

    print(f"Success Rate   : {success_rate:.2f}%")

    print("=" * 70)