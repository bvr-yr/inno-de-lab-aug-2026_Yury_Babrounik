BEGIN;

-- ====================== step 1 =========================
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
    -- or set UNIQUE in separate call if we want custom constraint name:
    -- CONSTRAINT UQ_Departments_DepartmentName UNIQUE (DepartmentName)
);


-- ====================== step 2 =========================
ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);


SAVEPOINT before_populating_email;

-- ====================== step 3 =========================
-- safely auto-generate using PG-specific CONCAT_WS():
UPDATE Employees
SET
    Email
    = CASE
        WHEN
            TRIM(Firstname) = ''
            AND TRIM(Lastname) = ''
            THEN NULL
        ELSE
            LOWER(
                CONCAT_WS(
                    '.',
                    NULLIF(TRIM(Firstname), ''),
                    NULLIF(TRIM(Lastname), '')
                ) || '@awesomestartup.com'
            )
    END
RETURNING Employees.Email;

-- acts as uniqueness self-check
ALTER TABLE Employees
ADD CONSTRAINT UQ_Employees_Email UNIQUE (Email);


ROLLBACK TO before_populating_email;


-- or simply populate with predefined values:
UPDATE Employees AS E
SET Email = V.Email
FROM
    (
        VALUES
        (1, 'famously.lusty.fieldmouse@awesomestartup.com'),
        (2, 'militantly.erudite.tench@awesomestartup.com'),
        (3, 'excellently.definitive.boatbill@awesomestartup.com'),
        (4, 'erectly.upstanding.whiting@awesomestartup.com'),
        (5, 'patiently.stalwart.waterfowl@awesomestartup.com'),
        (6, 'fleetingly.casual.bushbuck@awesomestartup.com'),
        (7, 'relevantly.exclusive.setter@awesomestartup.com'),
        (8, 'hoarsely.parental.gnu@awesomestartup.com'),
        (9, 'faultily.decisive.hare@awesomestartup.com'),
        (10, 'audaciously.miraculous.wildcat@awesomestartup.com')
    ) AS V (EmployeeID, Email)
WHERE
    E.EmployeeID = V.EmployeeID
RETURNING E.Email;


-- ====================== step 4 =========================
ALTER TABLE Employees
ADD CONSTRAINT UQ_Employees_Email UNIQUE (Email);


-- ====================== step 5 =========================
ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;


SELECT OfficeLocation
FROM
    Departments;

COMMIT;
