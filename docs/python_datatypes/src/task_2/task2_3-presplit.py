#!/usr/bin/env python

import sys

raw_transactions = sys.stdin.read().splitlines()

sanitized_transactions = [
    amount_int
    for transaction in raw_transactions
    for status, amount in [transaction.split(":")]
    if status == "SUCCESS" and (amount_int := int(amount)) > 0
]
