SELECT
    s.status,
    c.first_name,
    c.last_name
FROM
    shippings AS s
    INNER JOIN
        customers AS c
        ON s.customer = c.customer_id
-- To match task example result, though it's not required by task condition.
ORDER BY
    c.age;
