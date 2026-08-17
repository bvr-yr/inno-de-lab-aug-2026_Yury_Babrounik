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
