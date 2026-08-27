#!/usr/bin/env python

import sys

raw_transactions = sys.stdin.read().splitlines()

sanitized_transactions = [
    amount
    for transaction in raw_transactions
    if transaction.startswith("SUCCESS:")
    and (amount := int(transaction[8:])) > 0
]
