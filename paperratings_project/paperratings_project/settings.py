"""
For more information on this file, see: 
- https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see: 
- https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'i9$-mvdj^n$sphub4h)(l0ppl1uq_ii2!d#ov^_4v1i=_(wpo)')
# - set it locally: see under "Django app example" at https://mikebarkas.dev/2016/set-environment-variables-activating-virtualenv/
#  - however, with "venv", set in the "activate" file instead (not the activate.bat)
#    export SECRET_KEY='&ltc08quhgekn@2woi_62-fu@yfpp0$woj31x_@r^9e+hfl-o'
# - generate secret keys in python, >>> import secrets, >>> secrets.token_hex(24)

# About different shells and using venv (activate vs activate.bat, etc.): https://docs.python.org/3/library/venv.html


# DEBUG = True 
DEBUG = (os.environ.get('DJANGO_DEBUG', "True") == "True") # -> if DJANGO_DEBUG is "True" ->  Boolean True (DEBUG must be set to a boolean)
print("DEBUG: ", DEBUG)

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'funky-django-react.herokuapp.com'
]

# LOGGING = { 'version': 1, 'disable_existing_loggers': False, 'handlers': { 'file': { 'level': 'DEBUG', 'class': 'logging.FileHandler', 'filename': '/tmp/debug.log', }, }, 'loggers': { 'django': { 'handlers': ['file'], 'level': 'DEBUG', 'propagate': True, }, }, }


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'knox',
    'accounts',
    'papers',
    #'frontend', # not set up as a django app, added below in TEMPLATES -> DIRS & included in the base urls.py as url('', TemplateView.as_view(template_name="index.html")),
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': 
    ('knox.auth.TokenAuthentication',) # Note, needs to be a tuple, thus the trailing comma
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'paperratings_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend', 'templates', 'frontend')],
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

WSGI_APPLICATION = 'paperratings_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Deploying to Heroku: Update database configuration using python package "dj-database-url"
db_from_env = dj_database_url.config(conn_max_age=500) #, ssl_require=True
print("db_from_env: ", db_from_env)
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


######################################################
# Static files (CSS, JavaScript, Fonts, Images, ...) # - https://docs.djangoproject.com/en/3.0/howto/static-files/
######################################################
# *** PRODUCTION ***
# ******************
# Deploying Django to production (including the "whitenoise" package) - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment

# For production it is necessary to specify STATIC_ROOT, https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/
# - STATIC_ROOT - "The absolute path to the directory where collectstatic (python manage.py collectstatic) will collect static files for deployment." - https://docs.djangoproject.com/en/3.0/ref/settings/#static-files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Django and Static Assets, to serve Media files on Heroku - https://devcenter.heroku.com/articles/django-assets
# - WhiteNoise official docs - http://whitenoise.evans.io/en/stable/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# *******************
# *** DEVELOPMENT *** (i.e. running locally)
# *******************
# During development, paths to static files are specified in STATIC_URL and STATICFILES_DIRS
STATIC_URL = '/static/'

# static files that aren't tied to any particular [django] app, but to the purely React-based /frontend subfolder
# - https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'static', 'frontend'),
]


###############
# Media files #
############### 
# First example: the Corey Schafer tutorial at https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1


# where uploaded files will be stored on the file system
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # BASE_DIR set by django
# how we're going to access the media files in the browser
MEDIA_URL = '/media/'