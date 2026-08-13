WITH
    -- CTE result: calculate first order_id for each item explicitly.
    orders_with_first_id AS (
        SELECT
            item,
            COUNT(*)              AS count,
            -- Using ROUND by intent.
            ROUND(AVG(amount), 2) AS avg_amount,
            MIN(order_id)         AS first_order_id
        FROM
            orders
        GROUP BY
            item
    )

SELECT
    item,
    count,
    avg_amount
FROM
    orders_with_first_id
ORDER BY
    first_order_id;
