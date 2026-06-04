from .base import *

from decouple import config


DEBUG = True
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# configuração para cookies/sessions
CORS_ALLOW_CREDENTIALS = True
