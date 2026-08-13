SELECT
    item,
    COUNT(*)              AS count,
    -- Used TRUNC here to match example, which simply cuts off digits.
    -- Instead, to avoid rounding errors (416.66 vs 416.67) I'd use:

    -- ROUND(AVG(amount), 2) AS avg_amount
    -- AVG(amount)::numeric(12, 2) AS avg_amount -- less type-safe
    TRUNC(AVG(amount), 2) AS avg_amount
FROM
    orders
GROUP BY
    item
/*
To match task example result, though it's not required by task condition.
Use each item's earliest (first-seen) order_id as grouping sort key.
See p3_task2_v2_cte.sql for another approach with exposed order logic.
*/
ORDER BY
    MIN(order_id);
