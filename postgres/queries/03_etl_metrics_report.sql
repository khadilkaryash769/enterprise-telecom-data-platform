-- ETL execution metrics report

SELECT
    pipeline_name,
    run_id,
    source_records,
    processed_records,
    rejected_records,
    status,
    started_at,
    completed_at,
    created_at
FROM etl_metrics
ORDER BY created_at DESC;
