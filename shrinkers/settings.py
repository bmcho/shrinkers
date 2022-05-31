"""
Django settings for shrinkers project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-m(^fqy)og6c96fwk=z(1fsqnzsi0^!a)2b6kxsjm(jwgn49t0j"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# ALLOWED_HOSTS = []
ENV = os.environ.get("DJANGO_ENV", "dev")

if ENV == "dev":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition
# AUTH_USER_MODEL = "shortener.Users"
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shortener.apps.ShortenerConfig",
    "django_user_agents",
    "drf_yasg",
    "rest_framework",
]

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
        "django_seed",
    ]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
}

if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]  # Django Debug Toolbar

LOGIN_URL = "/login"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # per-side cache
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
    "shortener.middleware.ShrinkersMiddleware",
]

if DEBUG:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",  # Django Debug Toolbar
    ]

GEOIP_PATH = os.path.join(BASE_DIR, "geolite2")


ROOT_URLCONF = "shrinkers.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shrinkers.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["DBNAME"],
        "USER": os.environ["DBUSER"],
        "PASSWORD": os.environ["PASSWORD"],
        "HOST": os.environ["DBHOST"],
        "PORT": os.environ["DBPORT"],
        "OPTION": {"autocommit": True, "charset": "utf8mb4"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# STATIC_URL = "static/"
# temp = False
if DEBUG:
    # 지금은 static을 무조건 구글gcp 에서 가져오고 있음
    # 로컬에 static을 두니깐 .. git이 너무 느려
    STATIC_URL = "static/"

    EMAIL_ID = ""
    EMAIL_PW = ""

else:
    keys = json.load(open(os.path.join(BASE_DIR, "service_keys.json")))

    try:
        EMAIL_ID = keys.get("email")
        EMAIL_PW = json.load(open(os.path.join(BASE_DIR, "service_keys.json"))).get("email_pw")
    except Exception:
        EMAIL_ID = None
        EMAIL_PW = None

    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(keys.get("service_key"))
    DEFAULT_FILE_STORAGE = "config.storage_backends.GoogleCloudMediaStorage"
    STATICFILES_STORAGE = "config.storage_backends.GoogleCloudStaticStorage"
    GS_STATIC_BUCKET_NAME = "shrinkers-api-bk"
    STATIC_URL = "https://storage.googleapis.com/{}/statics/".format(GS_STATIC_BUCKET_NAME)

# 'django-storages[google]'
#  google-auth

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Filesystem caching
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
#         "LOCATION": os.path.join(BASE_DIR, "cache_file"),
#     }
# }


# Local-memory caching
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
#         "LOCATION": "unique-snowflake",
#     }
# }
