import logging
import pandas as pd


def validate_customers(df):

    logging.info("Validation Started")

    valid_records = []
    invalid_records = []

    for _, row in df.iterrows():

        errors = []

        # Email check
        if pd.isna(row["email"]) or "@" not in str(row["email"]):
            errors.append("Invalid Email")

        # Phone check
        if len(str(row["phone_number"])) != 10:
            errors.append("Invalid Phone Number")

        # Plan check
        if row["plan_type"] not in ["PREPAID", "POSTPAID"]:
            errors.append("Invalid Plan Type")


        if errors:
            bad_row = row.to_dict()
            bad_row["error_reason"] = ", ".join(errors)
            invalid_records.append(bad_row)

        else:
            valid_records.append(row)


    valid_df = pd.DataFrame(valid_records)
    invalid_df = pd.DataFrame(invalid_records)


    logging.info(
        f"Validation Completed | Valid: {len(valid_df)} | Invalid: {len(invalid_df)}"
    )

    return valid_df, invalid_df