"""
Django settings for special_project project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-udip3ijuu9s6ief9n8$c15f6s$ny7k#+qm89-$u8ns2s)bcs)t"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['testing-django-project.onrender.com','*']


# Application definition

INSTALLED_APPS = [
    'tailwind',
    'theme',
    'django_browser_reload',
    'epidemic_stoper_system',
    'article_system',
    'account_system',
    'ai_diagnosis_app',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

TAILWIND_APP_NAME = 'theme'  # i made it
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # i made it

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # i made it
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "special_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "special_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

#DATABASES = {
#    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
#}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

#LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "my"  # i made it

TIME_ZONE = "Asia/Yangon"  # i made it

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'home'  # i made it
LOGOUT_REDIRECT_URL = 'login'  # i made it

INTERNAL_IPS = ["127.0.0.1"]  # i made it
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"  # i made it

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

#STATIC_URL = "static/"
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'  # i made it
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'theme/static')]  # i made it
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # i made it

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # i made it

AUTH_USER_MODEL = 'account_system.User_Account'  # i made it

MEDIA_URL = '/media/'  # i made it
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # i made it

SESSION_COOKIE_AGE = 6000  # i made it
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # i made it