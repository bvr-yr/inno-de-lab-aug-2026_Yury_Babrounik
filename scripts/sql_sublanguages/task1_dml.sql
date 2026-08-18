BEGIN;

-- ====================== step 1 =========================
INSERT INTO Employees (
    FirstName,
    LastName,
    Department,
    Salary
)
VALUES
('Ben', 'Evans', 'HR', 90000.00),
('Gregory', 'Richards', 'Finance', 89999.00);


-- ====================== step 2 =========================
SELECT --noqa: AM04,LT09
    *
FROM
    Employees;


-- ====================== step 3 =========================
SELECT
    FirstName,
    LastName
FROM
    Employees
WHERE
    Department = 'IT';


-- ====================== step 4 =========================
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


-- ====================== step 5 =========================
DELETE
FROM Employees
WHERE -- or:
    -- CONCAT(FirstName, ' ', LastName) = 'Eve Davis';
    -- EmployeeID = 5;
    FirstName = 'Eve'
    AND
    LastName = 'Davis'
RETURNING Employees.*;


-- ====================== step 6 =========================
SELECT --noqa: AM04,LT09
    *
FROM
    Employees;

COMMIT;
