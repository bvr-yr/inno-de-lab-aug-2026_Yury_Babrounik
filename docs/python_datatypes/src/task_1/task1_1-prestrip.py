#!/usr/bin/env python

import sys

for raw_user_record in sys.stdin:
    user_record = [field.strip() for field in raw_user_record.split(";")]

    """ UID """
    user_record[0] = f"UID-{user_record[0]}"

    """ NAME """
    user_record[1] = user_record[1].replace("_", " ").title()

    """ CITY """
    user_record[2] = user_record[2].upper()

    """ STATUS """
    user_record[3] = user_record[3].lower()

    normalized = f"Normalized record: {' | '.join(user_record)}"
