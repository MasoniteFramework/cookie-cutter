""" Database Settings """

import os

from masonite.environment import LoadEnvironment, env
from masoniteorm.query import QueryBuilder
from masoniteorm.connections import ConnectionResolver

"""
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
"""

LoadEnvironment()

"""
The connections here don't determine the database but determine the "connection".
They can be named whatever you want.
"""

DATABASES = {
    "default": "mysql",
    "mysql": {
        "driver": "mysql",
        "host": env('DB_HOST'),
        "user": env("DB_USERNAME"),
        "password": env("DB_PASSWORD"),
        "database": env("DB_DATABASE"),
        "port": env('DB_PORT'),
        "options": {
            "charset": "utf8mb4",
        },
    },
    "postgres": {
        "driver": "postgres",
        "host": env('DB_HOST'),
        "user": env("DB_USERNAME"),
        "password": env("DB_PASSWORD"),
        "database": env("DB_DATABASE"),
        "port": env('DB_PORT'),
        "prefix": "",
    },
    "sqlite": {"driver": "sqlite", "database": "orm.sqlite3", "prefix": ""},
}

db = ConnectionResolver().set_connection_details(DATABASES)

# DATABASES = {
#     'default': os.environ.get('DB_DRIVER'),
#     'sqlite': {
#         'driver': 'sqlite',
#         'database': os.environ.get('DB_DATABASE')
#     },
#     'postgres': {
#         'driver': 'postgres',
#         'host': env('DB_HOST'),
#         'database': env('DB_DATABASE'),
#         'port': env('DB_PORT'),
#         'user': env('DB_USERNAME'),
#         'password': env('DB_PASSWORD'),
#         'log_queries': env('DB_LOG'),
#     },
# }

# DB = DatabaseManager(DATABASES)
# Model.set_connection_resolver(DB)
