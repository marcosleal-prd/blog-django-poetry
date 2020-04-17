import os

from pythonjsonlogger.jsonlogger import JsonFormatter
from request_id_django_log.filters import RequestIDFilter

from blog_python.support.django_helpers import eval_env_as_boolean

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if DJANGO_SECRET_KEY:
    SECRET_KEY = DJANGO_SECRET_KEY
else:
    raise NotImplementedError(f"You must configure DJANGO_SECRET_KEY!")

CSRF_COOKIE_SECURE = eval_env_as_boolean("CSRF_COOKIE_SECURE", True)
SESSION_COOKIE_SECURE = eval_env_as_boolean("SESSION_COOKIE_SECURE", True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval_env_as_boolean("DJANGO_DEBUG", False)
USE_STATIC_FILE_HANDLER_FROM_WSGI = eval_env_as_boolean(
    "USE_STATIC_FILE_HANDLER_FROM_WSGI", False
)

DJANGO_ALLOWED_HOSTS: str = os.getenv("DJANGO_ALLOWED_HOSTS")
if DJANGO_ALLOWED_HOSTS:
    ALLOWED_HOSTS = DJANGO_ALLOWED_HOSTS.split(",")
else:
    ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "request_id_django_log",
    "blog_python.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "blog_python.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "blog_python.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.getenv("DB_USER"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "CONN_MAX_AGE": int(os.getenv("DB_CONN_MAX_AGE", 0)),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
password_validation = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{password_validation}.UserAttributeSimilarityValidator"},
    {"NAME": f"{password_validation}.MinimumLengthValidator"},
    {"NAME": f"{password_validation}.CommonPasswordValidator"},
    {"NAME": f"{password_validation}.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = os.getenv("STATIC_URL", "/static/")

# Django Rest Framework
REST_FRAMEWORK = {
    "PAGE_SIZE": int(os.getenv("PAGE_SIZE", 20)),
    "DEFAULT_PAGINATION_CLASS": "drf_link_navigation_pagination"
    + ".LinkNavigationPagination",
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"request_id": {"()": RequestIDFilter}},
    "formatters": {
        "standard": {
            "()": JsonFormatter,
            "format": "%(levelname)-8s [%(asctime)s] "
            + "[%(request_id)s] %(name)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["request_id"],
            "formatter": "standard",
        }
    },
    "loggers": {
        "": {
            "level": os.getenv("ROOT_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
        },
        "blog_python": {
            "level": os.getenv("PROJECT_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
            "propagate": False,
        },
        "django": {
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
            "handlers": ["console"],
        },
        "django.request": {
            "level": os.getenv("DJANGO_REQUEST_LOG_LEVEL", "INFO"),
            "handlers": ["console"],
            "propagate": False,
        },
        "django.db.backends": {
            "level": os.getenv("DJANGO_DB_BACKENDS_LOG_LEVEL", "INFO"),
            "propagate": False,
            "handlers": ["console"],
        },
    },
}

# Request ID
REQUEST_ID_CONFIG = {
    "GENERATE_REQUEST_ID_IF_NOT_FOUND": True,
    "REQUEST_ID_HEADER": "HTTP_X_REQUEST_ID",
    "RESPONSE_HEADER_REQUEST_ID": "HTTP_X_REQUEST_ID",
}
