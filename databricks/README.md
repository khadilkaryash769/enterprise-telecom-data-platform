# Databricks Layer

This folder contains the Databricks/PySpark work reconstructed from the supplied
Databricks notebook screenshots.

Observed workflow:
S3 customers.csv -> Spark read -> data cleaning -> Delta -> Unity Catalog table
-> Silver data -> Gold aggregation by plan_type.

Observed results:
- Spark version: 4.1.0
- Source records: 10,000
- Gold aggregation shown:
  - POSTPAID: 4,922
  - PREPAID: 5,078

Note:
The files preserve the code and paths visible in the screenshots. They are
organized for the project; they are not a claim that unseen notebook cells
contained additional logic.
