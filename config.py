import os

config = {
    "api_key"           : "",
    "to_address"        : "",
    "from_address"      : "",
    "secret_key"        : "",
}

for key in config:
    if os.getenv(key) is not None:
        config[key] = os.getenv(key)

