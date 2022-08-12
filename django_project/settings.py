"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import django_heroku

import warnings
import logging
from pathlib import Path

# SSL redirect http to https
SECURE_SSL_REDIRECT = True


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = (os.environ.get('DEBUG_VALUE') == "True")


WHITENOISE_USE_FINDERS = True
# warnings.filterwarnings("ignore", message="No directory at", module="whitenoise.base" )
ALLOWED_HOSTS = ['caesar-first-web-app.herokuapp.com','caesarsyning.com']

SOCIALACCOUNT_LOGIN_ON_GET=True
# Application definition
INSTALLED_APPS = [
    'event.apps.EventConfig',
    'course.apps.CourseConfig',
    'resale.apps.ResaleConfig',
    'housing.apps.HousingConfig',
    'users.apps.UsersConfig',
    'home.apps.HomeConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'fontawesomefree',
    'django.contrib.sites', # <-- add the sites app here
    # apps needed for django all auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # add the below app for google authentication to work
    'allauth.socialaccount.providers.google',
    'django.contrib.postgres',
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    # django's inbuild authentication backend
    'django.contrib.auth.backends.ModelBackend',

    # django's allauth authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
ACCOUNT_FORMS = {'login': 'users.forms.MyCustomLoginForm'}
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_SESSION_REMEMBER= False
#django-allauth registraion settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# staticfiles where heroku put the static files 
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# os.path.join ensure the directory created correctly no matter what os you are using
# BASE_DIR is a variable in django like User, this means the 'media' will be 
# located in this BASE_DIR, and  a profile_pic will be created inside this folder
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# this represent how to access the pics in this directory
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK =  'bootstrap4'

LOGOUT_REDIRECT_URL = 'account_login'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'account_login'

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True


SERVER_EMAIL = 'django@my-domain.example'

ADMINS = (
    ('Caesar','siyuan.ning@menlo.edu'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
                 '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/www/logs/ibiddjango.log',
            'maxBytes': 1024000,
            'backupCount': 3,
        },
        'sql': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/www/logs/sql.log',
            'maxBytes': 102400,
            'backupCount': 3,
        },
        'commands': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/www/logs/commands.log',
            'maxBytes': 10240,
            'backupCount': 3,
        },
        'mail_admins': {
             'level': 'ERROR',
             'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console', 'mail_admins'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['sql', 'console'],
            'propagate': False,
            'level': 'WARNING',
        },
        'scheduling': {
            'handlers': ['commands', 'console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

POST_CATEGORY_CHOICES = (
     ("ask", "ask"),
    ("bid", "bid"),
)

EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

AWS_ACCESS_KEY_ID= os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME= os.environ.get('AWS_STORAGE_BUCKET_NAME')

SITE_ID = 1
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')

AWS_S3_FIE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


django_heroku.settings(locals())

# Activate Django-Heroku.
# Use this code to avoid the psycopg2 / django-heroku error!  
# Do NOT import django-heroku above!
# try:
#     if 'HEROKU' in os.environ:
#         import django_heroku
#         django_heroku.settings(locals())
# except ImportError:
#     found = False

