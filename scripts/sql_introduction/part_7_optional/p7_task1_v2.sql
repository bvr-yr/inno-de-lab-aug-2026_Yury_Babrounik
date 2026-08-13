WITH
    -- CTE result: summary table with total orders and amount per customer.
    total_by_customer AS (
        SELECT
            customer_id,
            COUNT(*)    AS total_orders,
            SUM(amount) AS total_amount
        FROM
            orders
        GROUP BY
            customer_id
    ),

    -- CTE result: optimize by deduping here *before* joining.
    delivered_customers AS (
        SELECT DISTINCT customer
        FROM
            shippings
        WHERE
            status = 'Delivered'
    )

SELECT --noqa: ST06
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    t.total_orders,
    t.total_amount
FROM
    total_by_customer AS t
    INNER JOIN
        delivered_customers AS d
        ON t.customer_id = d.customer
    INNER JOIN
        customers AS c
        ON t.customer_id = c.customer_id
WHERE
    t.total_orders >= 2;
