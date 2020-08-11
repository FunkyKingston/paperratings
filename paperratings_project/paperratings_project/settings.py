"""
Django settings for paperratings_project project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# with Debug = False -> I get the following errors
# - Refused to apply style from 'http://localhost:8000/static/css/main.css' because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.   http://localhost:8000/
# - Refused to execute script from 'http://localhost:8000/static/main.js' because its MIME type ('text/html') is not executable, and strict MIME type checking is enabled.   http://localhost:8000/
# import mimetypes
# mimetypes.add_type("text/css", ".css", True) # does this write to Regedit? (Windows)
# and something like..(?)   mimetypes.add_type("application/javascript", ".js", True) 



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = &ltc08quhgekn@2woi_62-fu@yfpp0$woj31x_@r^9e+hfl-ov
# SECRET_KEY = os.environ['DJANGO_SECRET_KEY'] # Specify at the Heroku app's settings (to do locally, add to venv's activate file)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'i9$-mvdj^n$sphub4h)(l0ppl1uq_ii2!d#ov^_4v1i=_(wpo)')
# - set it locally: see under "Django app example" at https://mikebarkas.dev/2016/set-environment-variables-activating-virtualenv/
#  - however, with "venv", set in the "activate" file instead (not the activate.bat)
#    export SECRET_KEY='&ltc08quhgekn@2woi_62-fu@yfpp0$woj31x_@r^9e+hfl-o'

# About different shells and using venv (activate vs activate.bat, etc.): https://docs.python.org/3/library/venv.html


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
    #'frontend', # not set up as a django app, added under TEMPLATE 'DIRS' & included in the base urls.py as url('', TemplateView.as_view(template_name="index.html")),
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': 
    ('knox.auth.TokenAuthentication',) # OBS! måste ha med , efter här för att göra till en tuple (med ett element)
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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


# Static files (CSS, JavaScript, Fonts, Images, ...)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# - For production: https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/
#   - STATIC_ROOT - "The absolute path to the directory where collectstatic (python manage.py collectstatic) will collect static files for deployment." - https://docs.djangoproject.com/en/3.0/ref/settings/#static-files

# For production (DEBUG = False), we need to specify a place, STATIC_ROOT, where the static files will be placed by collectstatic - https://youtu.be/Sa_kQheCnds?t=2340
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # try path that isn't same as STATIC_URL
# - in production (DEBUG = True), we need to specify a path to where our static files should be stored
#  - dock är de fortfarande "hostade" (?) på URL "STATIC_URL", d.v.s. t.ex. på URL .../static/main.js

# For Heroku - DJANGO AND STATIC ASSETS (including the "whitenoise" package) - https://devcenter.heroku.com/articles/django-assets
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # "Where Heroku puts static files" (? or rather, where it expects them to be? I guess django decides where python manage.py collectstatics put them? to where STATIC_ROOT points?)


# During development, static files in STATIC_URL and STATICFILES_DIRS
STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage' # add 'whitenoise' package to requirements.txt, see e.g. https://www.youtube.com/watch?v=r0ECufCyyyw
# - ALSO DO: add to wsgi.py, from whitenoise.django import DjangoWhiteNoise, application = DjangoWhiteNoise(application)

# static files that aren't tied to any particular [django] app, but to the purely React-based /frontend subfolder
# - https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'static', 'frontend'),
]

# media files, inspired by the Corey Schafer tutorial at https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1
# where uploaded files will be stored on the file system
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # BASE_DIR set by django
# how we're going to access the media files in the browser
MEDIA_URL = '/media/'