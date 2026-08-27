#!/usr/bin/env python

import sys

for raw_user_record in sys.stdin:
    user_record = raw_user_record.split(";")

    user_record[0] = f"UID-{user_record[0].strip()}"
    user_record[1] = user_record[1].strip().replace("_", " ").title()
    user_record[2] = user_record[2].strip().upper()
    user_record[3] = user_record[3].strip().lower()

    normalized = f"Normalized record: {' | '.join(user_record)}"
