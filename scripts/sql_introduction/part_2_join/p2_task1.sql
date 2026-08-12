SELECT
    c.first_name,
    c.last_name,
    o.item,
    o.amount
FROM
    orders AS o
    INNER JOIN
        customers AS c
        ON o.customer_id = c.customer_id;
