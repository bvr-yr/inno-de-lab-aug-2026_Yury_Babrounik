--noqa: disable=CP02,LT02

BEGIN;

-- uncomment to run ./tests/t3_transaction.sql:
-- REVOKE ALL PRIVILEGES ON Employees FROM hr_user;

DROP ROLE IF EXISTS hr_user;


-- ====================== step 1 =========================
CREATE ROLE hr_user
    LOGIN
    PASSWORD 'i1ov3inn0';


-- ====================== step 2 =========================
GRANT
    SELECT
ON Employees
TO hr_user;


SAVEPOINT before_granting_write;

-- ====================== step 3 =========================
-- test 1: ./tests/t1_select.sql
-- test 2: ./tests/t2_insert.sql


-- ====================== step 4 =========================
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

-- ====================== step 5 =========================
-- test 3: ./tests/t3_transaction.sql

-- comment out to run ./tests/t3_transaction.sql:
ROLLBACK TO SAVEPOINT before_granting_write;

COMMIT;
