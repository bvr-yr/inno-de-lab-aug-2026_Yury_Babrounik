#!/usr/bin/env python

import sys

for raw_user_record in sys.stdin:
    uid_raw, name_raw, city_raw, status_raw = [
        field.strip() for field in raw_user_record.split(";")
    ]

    uid = f"UID-{uid_raw}"
    name = name_raw.replace("_", " ").title()
    city = city_raw.upper()
    status = status_raw.lower()

    normalized = f"Normalized record: {' | '.join([uid, name, city, status])}"
