-- Customer summary by plan type

SELECT
    plan_type,
    COUNT(*) AS customer_count
FROM customers
GROUP BY plan_type
ORDER BY plan_type;
