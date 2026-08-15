# Enterprise Telecom Data Platform

## Project Overview

This project simulates a production-oriented enterprise telecom data engineering platform.

The project covers data ingestion, ETL processing, data cleaning and validation, cloud-based processing with AWS S3 and Databricks, Delta Lake storage, Unity Catalog registration, PostgreSQL loading, SQL reporting, logging, and pipeline orchestration setup.

---

## Architecture

### High-Level Data Flow

```text
CSV / Excel / Database Exports
            |
            v
       Raw Data Layer
     (data/Raw or AWS S3)
            |
            v
     Python + PySpark ETL
   - Extraction
   - Transformation
   - Data Cleaning
   - Validation
   - Bad Record Handling
   - Metrics / Logging
            |
            +----------------------+
            |                      |
            v                      v
      PostgreSQL              Databricks
                                 |
                                 v
                           Delta Lake
                                 |
                                 v
                           Unity Catalog
                                 |
                                 v
                         Silver / Gold Data
            |
            v
       SQL Reporting
```

---

## Technology Stack

### Implemented / Used

- Python
- PySpark
- SQL
- PostgreSQL
- AWS S3
- Databricks
- Delta Lake
- Unity Catalog
- Docker / Docker Compose
- VS Code

### In Progress

- Apache Airflow for workflow orchestration

### Planned / Future Enhancements

- Apache Kafka for real-time data ingestion
- Power BI for dashboards and reporting

---

## Databricks & AWS S3

The project was extended from local development to a cloud-based data processing flow.

### AWS S3

Raw customer data was stored in an AWS S3 bucket.

Example:

```text
s3://enterprise-telecom-data-yash-2026/customers.csv
```

### Databricks

Databricks was used for PySpark-based data processing.

The Databricks workflow included:

1. Creating and using compute
2. Reading data from the Databricks volume / cloud storage
3. Reading customer data from AWS S3
4. Performing data quality and cleaning operations
5. Creating Delta data
6. Registering the processed data as a Unity Catalog table
7. Creating Silver and Gold transformations
8. Running SQL queries on the resulting table

---

## Data Cleaning

The PySpark processing includes operations such as:

- Removing duplicate records
- Removing records with NULL customer IDs
- Trimming spaces from string columns
- Standardizing email values
- Validating records
- Handling bad records

---

## Medallion-Style Processing

### Bronze / Raw

Raw customer data is retained before transformation.

### Silver

Cleaned and standardized customer records are stored in Delta format.

Typical operations include:

- Deduplication
- NULL validation
- String trimming
- Email standardization

### Gold

Business-level aggregations are generated from the cleaned Silver data.

Example:

```text
plan_type        customer_count
POSTPAID         4922
PREPAID          5078
```

---

## Unity Catalog

The processed Delta data was registered as a Unity Catalog table.

Example table:

```text
enterprise_telecom_customers
```

This provides a governed catalog/table layer for querying the processed data in Databricks.

---

## PostgreSQL

PostgreSQL is used as the relational database layer for processed data and reporting-oriented tables.

The project also includes SQL scripts for table creation and reporting/ETL metrics.

---

## Python / PySpark Scripts

The `scripts/` directory contains the ETL and supporting Python/PySpark scripts.

Examples include:

```text
extract.py
incremental_extract.py
transform.py
validate.py
load.py
main.py

spark_extract.py
spark_transform.py
spark_validate.py
spark_load.py
spark_main.py
spark_metadata.py
spark_metadata_update.py
spark_metrics.py
spark_logger.py
```

---

## SQL

The `sql/` directory contains SQL scripts used for database objects and reporting/ETL-related queries.

---

## Logging & Data Quality

The project includes logging and validation components for:

- ETL execution
- Data validation
- Error handling
- Bad record handling
- ETL metrics

---

## Orchestration

Apache Airflow is part of the target architecture and its setup is currently in progress.

Target workflow:

```text
Start / Trigger
      |
      v
Ingest Raw Data
      |
      v
Run PySpark Jobs
      |
      v
Validate Data
      |
      v
Load to PostgreSQL
      |
      v
Generate Reports
      |
      v
End
```

---

## Project Structure

```text
enterprise-telecom-data-platform/
|
├── airflow/
├── architecture/
├── config/
├── data/
├── databricks/
├── docker/
├── docs/
├── kafka/
├── logs/
├── postgres/
├── powerbi/
├── python/
├── scripts/
├── spark/
├── sql/
├── .env
├── .gitignore
├── docker-compose.yml
└── README.md
```

---

## Future Enhancements

The following components are planned for future enhancement:

- Apache Kafka for real-time streaming
- Power BI dashboards
- Complete Airflow orchestration and scheduling
- Further production hardening and deployment automation

---

## Development Environment

Development, coding, testing, and execution are primarily performed using VS Code.

The project contains multiple iterations of the ETL implementation, with the final architecture combining local Python/PySpark development with AWS S3 and Databricks-based processing.

---

## Project Status

| Component | Status |
|---|---|
| Python ETL | Implemented |
| PySpark ETL | Implemented |
| Data Cleaning | Implemented |
| Data Validation | Implemented |
| AWS S3 | Implemented |
| Databricks | Implemented |
| Delta Lake | Implemented |
| Unity Catalog | Implemented |
| PostgreSQL | Implemented |
| SQL Reporting | Implemented |
| Logging / Metrics | Implemented |
| Airflow | Setup / In Progress |
| Kafka | Planned |
| Power BI | Planned |

---

## Author

Yash Jayant Khadilkar
