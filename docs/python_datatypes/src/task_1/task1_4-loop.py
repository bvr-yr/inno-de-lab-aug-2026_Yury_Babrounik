#!/usr/bin/env python

import sys

for raw_user_record in sys.stdin:
    user_record = raw_user_record.split(";")

    for i, field in enumerate(user_record):
        match i:
            case 0:
                user_record[0] = f"UID-{field.strip()}"
            case 1:
                user_record[1] = field.strip().replace("_", " ").title()
            case 2:
                user_record[2] = field.strip().upper()
            case 3:
                user_record[3] = field.strip().lower()

    normalized = f"Normalized record: {' | '.join(user_record)}"
