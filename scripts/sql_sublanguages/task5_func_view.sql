CREATE OR REPLACE FUNCTION CalculateAnnualBonus( --noqa: CP03
    p_employee_id INT,
    p_salary DECIMAL DEFAULT NULL
)
RETURNS DECIMAL(10, 2)
LANGUAGE Plpgsql
AS $$
DECLARE
    v_salary DECIMAL(10, 2);
BEGIN
    -- TODO: maybe RAISE when passed invalid ID instead of just NULL
    v_salary := COALESCE(
        p_salary, -- use this if passed directly, fallback to Employee lookup.
        (
            SELECT Salary
            FROM Employees
            WHERE EmployeeID = p_employee_id
        )
    );

    RETURN v_salary * 0.10;

    -- just in case Salary is actually monthly value.
    -- RETURN v_salary * 0.10 * 12;

END;
$$;


-- overloaded, DECIMAL only
CREATE OR REPLACE FUNCTION CalculateAnnualBonus( --noqa: CP03
    p_salary DECIMAL
)
RETURNS DECIMAL(10, 2)
LANGUAGE Plpgsql
AS $$
BEGIN
    RETURN p_salary * 0.10;
END;
$$;


SELECT CalculateAnnualBonus(EmployeeID, Salary) --noqa: CP03
FROM
    Employees;

SELECT CalculateAnnualBonus(EmployeeID) --noqa: CP03
FROM
    Employees;

SELECT CalculateAnnualBonus(Salary) --noqa: CP03
FROM
    Employees;

SELECT CalculateAnnualBonus(9999, NULL); --noqa: CP03


CREATE OR REPLACE
VIEW IT_Department_View AS
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary
FROM
    Employees
WHERE
    Department = 'IT';


SELECT --noqa: AM04,LT09
    *
FROM
    IT_Department_View;
