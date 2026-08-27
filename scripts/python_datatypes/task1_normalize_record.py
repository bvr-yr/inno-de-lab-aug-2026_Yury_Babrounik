raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "


# only split here, using strip() first for every part might be more logical,
# but better avoid overhead operations
user_record = raw_user_record.split(";")

# don't unpack here for the same reason
# access list elements directly by idx and just modify inplace
# string literals used here to keep script user-friendly and maintainable

""" UID """
user_record[0] = f"UID-{user_record[0].strip()}"

""" NAME """
user_record[1] = user_record[1].strip().replace("_", " ").title()

""" CITY """
user_record[2] = user_record[2].strip().upper()

""" STATUS """
user_record[3] = user_record[3].strip().lower()

# if input source is not fully trusted and records may contain unnecessary
# extra fields, use .join(user_record[:4]) instead
print(f"Normalized record: {' | '.join(user_record)}")
