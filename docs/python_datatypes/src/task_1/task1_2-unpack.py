#!/usr/bin/env python

import sys

for raw_user_record in sys.stdin:
    uid_raw, name_raw, city_raw, status_raw = raw_user_record.split(";")

    uid = f"UID-{uid_raw.strip()}"
    name = name_raw.strip().replace("_", " ").title()
    city = city_raw.strip().upper()
    status = status_raw.strip().lower()

    normalized = f"Normalized record: {' | '.join([uid, name, city, status])}"
