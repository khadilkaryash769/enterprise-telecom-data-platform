# PostgreSQL

This folder contains PostgreSQL-specific database initialization scripts and reporting queries for the Enterprise Telecom Data Platform.

## Structure

```text
postgres/
├── init/
│   ├── 01_create_tables.sql
│   └── 02_create_indexes.sql
├── queries/
│   ├── 01_customer_summary.sql
│   ├── 02_customer_city_summary.sql
│   └── 03_etl_metrics_report.sql
└── README.md
```

## Tables

### customers
Stores processed customer records used by the relational/reporting layer.

### etl_metrics
Stores ETL execution metrics such as source, processed and rejected record counts and pipeline status.

## Notes

The SQL files are designed to be safe to run more than once where practical by using `IF NOT EXISTS`.

Data loading is performed by the project's Python/PySpark ETL components; this folder contains the PostgreSQL database objects and reporting queries rather than the ETL Python code.
