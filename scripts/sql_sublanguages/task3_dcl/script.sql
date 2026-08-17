--noqa: disable=CP02,LT02

BEGIN;

-- uncomment to run ./tests/t3_transaction.sql:
REVOKE ALL PRIVILEGES ON Employees FROM hr_user;
DROP ROLE IF EXISTS hr_user;

CREATE ROLE hr_user
    LOGIN
    PASSWORD 'i1ov3inn0';


GRANT
    SELECT
ON Employees
TO hr_user;

SAVEPOINT before_granting_write;


GRANT
    INSERT,
    UPDATE
ON Employees
TO hr_user;


-- to deal with PG error caused by additional permissions
-- required, due to SERIAL type on EmployeeID Primary Key.
GRANT
    USAGE,
    SELECT
ON SEQUENCE
    employees_employeeid_seq
TO hr_user;


-- comment out to run ./tests/t3_transaction.sql:
-- ROLLBACK TO SAVEPOINT before_granting_write;

COMMIT;
