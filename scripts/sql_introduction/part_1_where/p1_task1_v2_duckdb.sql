-- Assume we need all customer attributes except id,
-- or we accept the risk of future schema changes.
SELECT --noqa: AM04,LT09
    * EXCLUDE (customer_id)
FROM
    customers
WHERE
    country = 'USA'
    AND age > 25;
