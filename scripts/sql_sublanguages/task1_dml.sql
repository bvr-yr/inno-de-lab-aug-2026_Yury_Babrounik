BEGIN;

INSERT INTO Employees (
    FirstName,
    LastName,
    Department,
    Salary
)
VALUES
('Ben', 'Evans', 'HR', 90000.00),
('Gregory', 'Richards', 'Finance', 89999.00);


SELECT --noqa: AM04,LT09
    *
FROM
    Employees;


SELECT
    FirstName,
    LastName
FROM
    Employees
WHERE
    Department = 'IT';


UPDATE Employees
SET
    Salary = 65000.00
WHERE -- or:
    -- CONCAT(FirstName, ' ', LastName) = 'Alice Smith';
    -- EmployeeID = 1;
    FirstName = 'Alice'
    AND
    LastName = 'Smith'
RETURNING Employees.*; -- for a quick check


DELETE
FROM Employees
WHERE -- or:
    -- CONCAT(FirstName, ' ', LastName) = 'Eve Davis';
    -- EmployeeID = 5;
    FirstName = 'Eve'
    AND
    LastName = 'Davis'
RETURNING Employees.*;


SELECT --noqa: AM04,LT09
    *
FROM
    Employees;

COMMIT;
