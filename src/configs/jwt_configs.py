import os

jwt_infos = {
    "secret_key": os.getenv("JWT_SECRET_KEY"),
    "algorithm": os.getenv("JWT_ALGORITHM"),
    "expiration_time": int(os.getenv("JWT_EXPIRATION_TIME"))
}
