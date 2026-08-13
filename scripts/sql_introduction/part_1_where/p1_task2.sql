SELECT
    -- Alternatively use '*' here.
    order_id,
    item,
    amount,
    customer_id
FROM
    orders
WHERE
    amount > 1000;
