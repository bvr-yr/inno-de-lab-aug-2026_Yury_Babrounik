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
    )

/*
Dedup possible repeating rows after double-join,
if customer has several delivered shippments using DISTINCT keyword.
See p7_task1_v2.sql for another approach.
*/
SELECT DISTINCT --noqa: ST06
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    t.total_orders,
    t.total_amount
FROM
    total_by_customer AS t
    INNER JOIN
        shippings AS s
        ON t.customer_id = s.customer
    INNER JOIN
        customers AS c
        ON t.customer_id = c.customer_id
WHERE
    t.total_orders >= 2
    AND
    s.status = 'Delivered';
