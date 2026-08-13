-- Using cleaner aliasing here.
SELECT
    c.first_name,
    c.last_name,
    o1.amount
FROM
    customers AS c
    INNER JOIN
        orders AS o1
        ON c.customer_id = o1.customer_id
WHERE
    o1.amount = (
        SELECT --noqa: LT09
            MAX(o2.amount)
        FROM
            orders AS o2
    );
