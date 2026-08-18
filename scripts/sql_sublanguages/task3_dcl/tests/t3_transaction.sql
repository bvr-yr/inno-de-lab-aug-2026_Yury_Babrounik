BEGIN;

INSERT INTO Employees (
    FirstName,
    LastName,
    Department,
    Salary
)
VALUES (
    'Annie',
    'Douglas',
    'HR',
    1000.00
)
RETURNING Employees.*;


UPDATE Employees
SET
    Salary = 1100.00
WHERE
    FirstName = 'Annie'
    AND
    LastName = 'Douglas'
RETURNING Employees.*;


SELECT --noqa: AM04,LT09
    *
FROM
    Employees;

COMMIT;
