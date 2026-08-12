-- Listing columns explicitly as PostgreSQL requires.
-- See p1_task1_v2_duckdb.sql for another aproach.
SELECT
    first_name,
    last_name,
    age,
    country
FROM
    /*
    Despite Appendix A uses PascalCase for naming table during creation,
    PostgreSQL converts unquoted identifiers to lowercase. Acknowledging that
    I will use lowercase for convenience.

    PascalCase could be preserved by creating and referencing the table
    as double-quoted "Customers".
    */
    customers
WHERE
    country = 'USA'
    AND age > 25;
