requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
required_admin_roles = {"admin", "security_officer", "audit_manager"}

SEC_OFFICER_STR = "security_officer"

unique_requested_roles = set(requested_roles)

# or: unique_requested_roles & required_admin_roles
common_admin_roles = unique_requested_roles.intersection(required_admin_roles)

# or: required_admin_roles - unique_requested_roles
missing_admin_roles = required_admin_roles.difference(unique_requested_roles)

sec_officer_requested = SEC_OFFICER_STR in unique_requested_roles

print(f"Unique requested roles: {unique_requested_roles}")
print(f"    Common admin roles: {common_admin_roles}")
print(f"   Missing admin roles: {missing_admin_roles}")
print(f"Role {SEC_OFFICER_STR!r} is requested: {sec_officer_requested}")
