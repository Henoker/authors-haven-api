from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-j333@rnd&eo&n2@zw4syeug^6^*(%6*tot&h_nvpgdyxalg1#")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]