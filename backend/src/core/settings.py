"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from decouple import config
from datetime import datetime, timedelta

from rest_framework.permissions import IsAuthenticated

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["backend", "localhost"]


# Application definition

INSTALLED_APPS = [
    # ---- DEFAULT ----
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ---- Django REST Framework ----
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',


    'drf_spectacular', #? for swagger documentation

    # ---- Django AllAuth ----
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    #"allauth.socialaccount.providers.google",
    #"allauth.mfa",
    # "allauth.headless",
    # "allauth.usersessions",


    # ---- Application Apps ----
    'apps.authentication',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #! must be present for admin application
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #? ALLAUTH
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': config("POSTGRES_DB_NAME"),
        'USER': config("POSTGRES_USERNAME"),
        'PASSWORD': config("POSTGRES_PASSWORD"),
        'HOST': config("POSTGRES_HOST"),
        'PORT': config("POSTGRES_PORT")
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

#! ADDED
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    
    'DEFAULT_AUTHENTICATION_CLASSES': [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],

    #? COMMENTED
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]
}

REST_AUTH = {
    'REGISTER_SERIALIZER': "apps.authentication.api.serializers.CustomRegisterSerializer",
    'USER_DETAILS_SERIALIZER': 'apps.authentication.api.serializers.UserSerializer',
    'LOGIN_SERIALIZER': "apps.authentication.api.serializers.CustomLoginSerializer",
    "SESSION_LOGIN": False,

    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "jwt-access-token",
    "JWT_AUTH_REFRESH_COOKIE": "jwt-refresh-token",
    "JWT_AUTH_SECURE": True,
    "JWT_AUTH_HTTPONLY": True, 
}

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'apps.authentication.api.serializers.CustomPasswordResetSerializer'
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'BLACKLIST_AFTER_ROTATION': True,

    #? ADDED
    'SIGNING_KEY': config('JWT_SIGNING_KEY')
}




# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#! Added
# CSRF_COOKIE_SAMESITE = "Strict"
# SESSION_COOKIE_SAMESITE = "Strict"
# CSRF_COOKIE_HTTPONLY = True
# SESSION_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost',
    #'https://productionurl.com'
]

#* Prod only
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

SITE_ID = 1


AUTHENTICATION_BACKENDS = ([
    #"allauth.account.auth_backends.AuthenticationBackend",
    'django.contrib.auth.backends.ModelBackend',
])









#? ADDED
SPECTACULAR_SETTINGS = {
    #'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAdminUser'],  # Only admin users
    'SERVE_AUTHENTICATION': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ]
}


# ---- SMTP Configuration ----
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('GOOGLE_SMTP_APP_EMAIL')
EMAIL_HOST_PASSWORD = config('GOOGLE_SMTP_APP_PASS')

# ---- Django Configuration ----
AUTH_USER_MODEL = "authentication.User" #? custom user model
LOGIN_URL = "/login" #? login URL for Django's authentication system

# ---- dj-rest-auth Configuration ----
FRONTEND_URL = "http://localhost"
FRONTEND_RESET_PASSWORD_URL = "https://localhost/account/reset-password"
#PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = "http://localhost/account/reset-password/confirm"

# ---- Django AllAuth Configuration ----
EMAIL_CONFIRM_REDIRECT_BASE_URL = \
    "http://localhost/email/confirm/"


PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = \
    "http://localhost/account/password-reset/confirm/"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_METHODS = ['email'] #? user logs in with email instead of username
ACCOUNT_USERNAME_REQUIRED = False #? disables username field
ACCOUNT_USER_MODEL_USERNAME_FIELD = None #? removes username field from user model
ACCOUNT_UNIQUE_EMAIL = True #? no duplicate emails
ACCOUNT_CONFIRM_EMAIL_ON_GET = True #? confirms an email address when confirmation link is clicked
ACCOUNT_EMAIL_CONFIRMATION_TEMPLATE = "templates/account/email_confirmation_message.txt" #? custom email template
ACCOUNT_ADAPTER = "apps.authentication.adapters.CustomAccountAdapter" #? custom adapter logic