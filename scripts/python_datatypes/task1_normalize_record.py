raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "


# only split here, there are only 4 fields so I choose separate strips
user_record = raw_user_record.split(";")

# UID
user_record[0] = f"UID-{user_record[0].strip()}"

# NAME
user_record[1] = user_record[1].strip().replace("_", " ").title()

# CITY
user_record[2] = user_record[2].strip().upper()

# STATUS
user_record[3] = user_record[3].strip().lower()

print(f"Normalized record: {' | '.join(user_record)}")
