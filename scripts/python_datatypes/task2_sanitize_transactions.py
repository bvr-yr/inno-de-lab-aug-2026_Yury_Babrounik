raw_transactions = [
    "SUCCESS:100",
    "FAILED:50",
    "SUCCESS:-10",
    "SUCCESS:0",
    "SUCCESS:250",
    "ERROR:200",
]

PREFIX = "SUCCESS:"

sanitized_transactions = [
    amount
    for transaction in raw_transactions
    # here .startswith() acts as pre-filter for fixed format STATUS:AMOUNT
    if transaction.startswith(PREFIX)
    # assign variable once with ':=' right in expression
    # this helps to avoid double-parsing: in condition and
    # later in the final expression
    and (amount := int(transaction.removeprefix(PREFIX))) > 0
]

print(f"Sanitized transactions: {sanitized_transactions}")
