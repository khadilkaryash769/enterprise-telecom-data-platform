-- Indexes for commonly queried customer/reporting columns

CREATE INDEX IF NOT EXISTS idx_customers_email
    ON customers (email);

CREATE INDEX IF NOT EXISTS idx_customers_city
    ON customers (city);

CREATE INDEX IF NOT EXISTS idx_customers_plan_type
    ON customers (plan_type);

CREATE INDEX IF NOT EXISTS idx_etl_metrics_pipeline_name
    ON etl_metrics (pipeline_name);

CREATE INDEX IF NOT EXISTS idx_etl_metrics_created_at
    ON etl_metrics (created_at);
