SELECT
    country,
    -- To match example column name.
    -- "count" is a bit generic so I'd choose "client_count" or "customer_count"
    COUNT(*) AS count
FROM
    customers
GROUP BY
    country
-- To match task example result, though it's not required by task condition.
ORDER BY
    count DESC,
    country DESC; -- or only this.
