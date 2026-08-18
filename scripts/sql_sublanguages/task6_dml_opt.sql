-- ====================== step 1 =========================
SELECT P.ProjectName
FROM
    Projects AS P
    INNER JOIN
        EmployeeProjects AS EP
        ON P.ProjectID = EP.ProjectID
    INNER JOIN
        Employees AS E
        ON EP.EmployeeID = E.EmployeeID
WHERE
    E.FirstName = 'Bob'
    AND E.LastName = 'Johnson'
    AND EP.HoursWorked > 150;


BEGIN;

-- ====================== step 2 =========================
WITH
    IT_Projects AS (
        SELECT DISTINCT Ep.Projectid
        FROM
            EmployeeProjects AS Ep
            INNER JOIN
                Employees AS E
                ON Ep.EmployeeID = E.EmployeeID
        WHERE
            E.Department = 'IT'

    )

UPDATE Projects AS P
SET Budget = Budget * 1.10
FROM
    IT_Projects AS I
WHERE
    I.ProjectId = P.ProjectId
RETURNING P.*;


-- ====================== step 3 =========================
UPDATE Projects
SET
    EndDate = (StartDate + INTERVAL '1 year')::DATE
WHERE
    EndDate IS NULL
RETURNING Projects.*;

COMMIT;


-- ====================== step 4 =========================
BEGIN;

WITH
    Inserted_Employee AS (
        INSERT INTO Employees (
            FirstName,
            LastName,
            Department,
            Salary
        )
        VALUES (
            'Cole',
            'Deschanel',
            'IT',
            77777.00
        )
        RETURNING EmployeeID
    ),

    Target_Project AS (
        SELECT ProjectID
        FROM
            Projects
        WHERE
            -- Probably a good idea to add UNIQUE (ProjectName)
            ProjectName = 'Website Redesign'
    )

INSERT INTO EmployeeProjects (
    EmployeeID,
    ProjectID,
    HoursWorked
)
SELECT
    I.EmployeeID,
    T.ProjectID,
    80 --noqa: AL03
FROM
    Inserted_Employee AS I
    CROSS JOIN
        Target_Project AS T
RETURNING EmployeeProjects.*;

COMMIT;
