db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres",
    },
}

# defined as consts to be config-like defaults; maybe ommit _DEFAULT
HOST_DEFAULT = "production-db.internal"
PORT_DEFAULT = 5432
SSL_MODE_DEFAULT = "verify-full"

# not sure how to treat config dict based on task condition,
# whether it is strictly defined or serves as a reference
# .get() with defaults, just in case
db_connection = db_config.get("connection", {})
host = db_connection.get("host", HOST_DEFAULT)
port = db_connection.get("port", PORT_DEFAULT)

# use empty dict as fallback in first .get() call, so chained 2nd .get()
# safely fallbacks to SSL_MODE_DEFAULT when 'ssl_settings' is missing
ssl_mode = db_config.get("ssl_settings", {}).get("ssl_mode", SSL_MODE_DEFAULT)

db_connection["user"] = "admin"
db_connection["max_connections"] = 100

print(f"SSL Mode: {ssl_mode}")
print("Connection parameters:")

for key, value in db_connection.items():
    print(f"* {key}: {value}")
