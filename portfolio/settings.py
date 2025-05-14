import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import dj_database_url

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ... các middleware khác ...
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DATABASES = {"default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))}

SECRET_KEY = os.environ.get("SECRET_KEY", "your-default-secret-key")

ALLOWED_HOSTS = [".onrender.com", "localhost", "127.0.0.1"]
