# Spark / PySpark

This folder represents the Spark processing layer of the
Enterprise Telecom Data Platform.

## Implementation

The PySpark ETL implementation is maintained in the `scripts/`
directory.

Key Spark processing scripts include:

- `spark_main.py`
- `spark_extract.py`
- `spark_transform.py`
- `spark_validate.py`
- `spark_metadata.py`
- `spark_metrics.py`

## Processing

The Spark layer is used for:

- Data extraction
- Data transformation
- Data validation
- Metadata handling
- Data quality checks
- ETL metrics and reporting

## Databricks

Databricks-based Spark processing, including S3 integration,
Delta processing and Unity Catalog work, is maintained separately
in the `databricks/` directory.