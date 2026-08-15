-- PostgreSQL initialization
-- Enterprise Telecom Data Platform

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone_number VARCHAR(30),
    email VARCHAR(255),
    city VARCHAR(100),
    plan_type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS etl_metrics (
    metric_id BIGSERIAL PRIMARY KEY,
    pipeline_name VARCHAR(150) NOT NULL,
    run_id VARCHAR(100),
    source_records BIGINT DEFAULT 0,
    processed_records BIGINT DEFAULT 0,
    rejected_records BIGINT DEFAULT 0,
    status VARCHAR(30),
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
