#!/usr/bin/env python

import sys

raw_transactions = sys.stdin.read().splitlines()

PREFIX = "SUCCESS:"

sanitized_transactions = [
    int(transaction.removeprefix(PREFIX))
    for transaction in raw_transactions
    if transaction.startswith(PREFIX)
    and int(transaction.removeprefix(PREFIX)) > 0
]
