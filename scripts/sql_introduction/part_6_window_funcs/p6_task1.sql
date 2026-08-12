SELECT
    order_id,
    customer_id,
    item,
    amount,
    SUM(amount) OVER (
        PARTITION BY customer_id
    ) AS total_by_customer
FROM
    orders
-- To match task example result, though it's not required by task condition.
ORDER BY
    order_id;
