import os
from masonite.environment import env

KEY = os.getenv("APP_KEY", "-RkDOqXojJIlsF_I8wWiUq_KRZ0PtGWTOZ676u5HtLg=")

HASHING = {
    "default": env("HASHING_FUNCTION", "bcrypt"),
    "bcrypt": {"rounds": 10},
    "argon2": {"memory": 1024, "threads": 2, "time": 2},
}