"""
Django settings for realestate project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.conf import settings; 
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'SECRET_KEY'
with open('realestate/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['ktmrealestate.herokuapp.com']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',
    'realtors.apps.RealtorsConfig',
    'listings.apps.ListingsConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'spam_filter.apps.SpamFilterConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'django.contrib.humanize',

# allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # providers
'allauth.socialaccount.providers.facebook',
'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'realestate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
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

WSGI_APPLICATION = 'realestate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.mysql',
   #     'NAME': 'realestate',
    #    'USER': 'root',
     #   'PASSWORD': '',
      #  'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
       # 'PORT': '3306',
    #}
#}



DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ktmrealestate',
            'USER':'postgres',
            'PASSWORD':'root',
            'HOST':'127.0.0.1',
            'PORT': '5432'
        }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS=[os.path.join(BASE_DIR,'realestate/static')]


# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


SITE_ID=1
LOGIN_REDIRECT_URL="dashboard"

# Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


# Save our media folder

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'


# Sending Email
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ktmrealestate78@gmail.com'
EMAIL_HOST_PASSWORD = 'ktmrealestate1'

django_heroku.settings(locals())


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES' : [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES':(
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     )
# }





