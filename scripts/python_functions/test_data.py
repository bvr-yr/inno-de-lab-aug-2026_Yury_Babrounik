"""Test data provided by task condition."""

TASK_1_DATA = [
    ("Academy Dinosaur", 30, 2.99, 0.00),
    ("Affair Prejudice", 40, 4.99, 0.10),
    ("Agent Truman", 10, 1.99, 0.00),
    ("African Egg", 50, 3.50, 0.20),
]

# Set 1 (Standard)
TASK_2_TEST_1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55},
]

# Set 2 (Equal values)
TASK_2_TEST_2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00},
]

# Set 3 (Single element)
TASK_2_TEST_3 = [
    {"category": "Drama", "total_sales": 500.00},
]

TASK_2_DATA = (TASK_2_TEST_1, TASK_2_TEST_2, TASK_2_TEST_3)

TASK_3_DATA = [
    ("Matrix", 5, 1.5),
    ("Inception", "five", 2.0),
    ("Avatar", 0, 2.5),
    (
        "Interstellar",
        [
            3,
        ],
        3.0,
    ),
]
