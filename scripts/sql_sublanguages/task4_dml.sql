-- very basic helper
CREATE OR REPLACE PROCEDURE ShowDeleteMessage(p_method TEXT) --noqa: CP03
LANGUAGE Plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Deleting with "%"', p_method;
END;
$$;

BEGIN;


-- ====================== step 1 =========================
UPDATE Employees
SET
    Salary = Salary * 1.1
WHERE
    Department = 'HR'
RETURNING Employees.*;


-- ====================== step 2 =========================
UPDATE Employees
SET
    Department = 'Senior IT'
WHERE
    Salary > 70000.00
RETURNING Employees.*;


SAVEPOINT before_delete;


-- ====================== step 3 =========================
CALL ShowDeleteMessage('WHERE IN');
DELETE
FROM Employees AS E1
WHERE
    E1.EmployeeID IN (
        SELECT --noqa: AM04,LT09
            E2.EmployeeID
        FROM
            Employees AS E2
            LEFT JOIN
                EmployeeProjects AS Ep
                ON E2.EmployeeID = Ep.EmployeeID
        WHERE
            Ep.EmployeeID IS NULL
    )
RETURNING E1.*;

ROLLBACK TO before_delete;


CALL ShowDeleteMessage('NOT EXISTS');
DELETE FROM Employees AS E
WHERE
    NOT EXISTS (
        SELECT 1
        FROM
            EmployeeProjects AS Ep
        WHERE
            Ep.EmployeeID = E.EmployeeID
    )
RETURNING E.*;

ROLLBACK TO before_delete;


CALL ShowDeleteMessage('CTE');
WITH
    Unassigned AS (
        SELECT E.EmployeeID
        FROM
            Employees AS E
            LEFT JOIN
                EmployeeProjects AS Ep
                ON E.EmployeeID = Ep.EmployeeID
        WHERE
            Ep.EmployeeID IS NULL
    )

DELETE FROM Employees AS E
USING Unassigned AS U
WHERE
    E.EmployeeID = U.EmployeeID
RETURNING E.*;


SELECT --noqa: AM04,LT09
    *
FROM
    Employees
ORDER BY
    EmployeeId;

COMMIT;


-- ====================== step 4 =========================
BEGIN;

WITH
    Inserted_Project AS (
        INSERT INTO Projects (
            ProjectName,
            Budget,
            StartDate,
            EndDate
        )
        VALUES (
            'New Year Onboarding',
            500000.00,
            '2026-09-01',
            '2026-12-31'
        )
        RETURNING ProjectID
    ),

    -- simply to avoid hardcoding values
    Random_Employees AS (
        SELECT EmployeeID
        FROM
            Employees
        ORDER BY
            RANDOM()
        LIMIT 2
    ),

    Random_Employees_Houred AS (
        SELECT
            EmployeeID,
            CASE ROW_NUMBER() OVER ()
                WHEN 1 THEN 137
                WHEN 2 THEN 83
            END AS Hours
        FROM
            Random_Employees
    )

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT
    R.EmployeeID,
    I.ProjectID,
    R.Hours
FROM
    Random_Employees_Houred AS R
    CROSS JOIN
        Inserted_Project AS I
RETURNING EmployeeProjects.*;


SELECT *
FROM
    EmployeeProjects;

COMMIT;
