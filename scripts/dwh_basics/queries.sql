-- 1. which service categories generate highest net revenue?
SELECT
    dsc.category_name,
    SUM(fs.net_amount) AS total_net_revenue
FROM
    fact_services AS fs
    INNER JOIN
        dim_service AS ds
        ON fs.service_sk = ds.service_sk
    INNER JOIN
        dim_service_category AS dsc
        ON ds.service_category_sk = dsc.service_category_sk
GROUP BY
    dsc.category_name
ORDER BY
    total_net_revenue DESC;


-- 2. which part of the day has the most service activity?
SELECT
    dt.part_of_day,
    COUNT(*) AS total_services
FROM
    fact_services AS fs
    INNER JOIN
        dim_time AS dt
        ON fs.service_time_sk = dt.time_sk
GROUP BY
    dt.part_of_day
ORDER BY
    total_services DESC;


-- 3. are delays during visits higher on weekends or on working days?
SELECT
    CASE
        WHEN dd.is_weekend THEN 'Weekend'
        ELSE 'Workday'
    END                         AS day_type,
    AVG(fv.total_delay_minutes) AS average_total_delay_minutes
FROM
    fact_visits AS fv
    INNER JOIN
        dim_date AS dd
        ON fv.date_started_sk = dd.date_sk
WHERE
    fv.total_delay_minutes IS NOT NULL
GROUP BY
    dd.is_weekend
ORDER BY
    average_total_delay_minutes DESC;


-- 4. what is revenue from clinical services provided to exotic pets?
SELECT SUM(fs.net_amount) AS clinical_exotic_revenue
FROM
    fact_services AS fs
    INNER JOIN
        dim_service AS ds
        ON fs.service_sk = ds.service_sk
    INNER JOIN
        dim_service_category AS dsc
        ON ds.service_category_sk = dsc.service_category_sk
    INNER JOIN
        dim_pet AS dp
        ON fs.pet_sk = dp.pet_sk
    INNER JOIN
        dim_species AS dsp
        ON dp.species_sk = dsp.species_sk
WHERE
    dsc.is_clinical = TRUE
    AND dsp.is_exotic = TRUE;


-- 5. which vets generated highest net revenue
-- and how many services they performed?
SELECT
    dv.vet_sk,
    dv.first_name,
    dv.last_name,
    SUM(fs.net_amount) AS total_net_revenue,
    COUNT(*)           AS service_count
FROM
    fact_services AS fs
    INNER JOIN
        dim_vet AS dv
        ON fs.vet_sk = dv.vet_sk
GROUP BY
    dv.vet_sk,
    dv.first_name,
    dv.last_name
ORDER BY
    total_net_revenue DESC;


-- example check that uses source_visit_id to join both facts
-- to compare visit total vs service total for the same visit
SELECT
    fv.source_visit_id,
    fv.visit_total_paid,
    SUM(fs.net_amount) AS services_total_net_amount
FROM
    fact_visits AS fv
    INNER JOIN
        fact_services AS fs
        ON fv.source_visit_id = fs.source_visit_id
GROUP BY
    fv.source_visit_id
ORDER BY
    fv.source_visit_id;
