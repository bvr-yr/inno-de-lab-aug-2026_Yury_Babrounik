db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres",
    },
}

SSL_MODE_DEFAULT = "verify-full"

db_connection = db_config["connection"]

# probably for later use
host = db_connection["host"]
port = db_connection["port"]

# use empty dict as fallback in first .get() call, so chained 2nd .get()
# safely fallbacks to SSL_MODE_DEFAULT when 'ssl_settings' is missing
ssl_mode = db_config.get("ssl_settings", {}).get("ssl_mode", SSL_MODE_DEFAULT)

db_connection["user"] = "admin"
db_connection["max_connections"] = 100

print(f"SSL Mode: {ssl_mode}")
print("Connection parameters:")

for key, value in db_connection.items():
    print(f"* {key}: {value}")
