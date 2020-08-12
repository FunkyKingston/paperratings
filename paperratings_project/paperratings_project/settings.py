"""
For more information on this file, see: 
- https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see: 
- https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# import dj_database_url


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

# SECURITY WARNING: keep the secret key used in production secret
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'i9$-mvdj^n$sphub4h)(l0ppl1uq_ii2!d#ov^_4v1i=_(wpo)')
# - set it locally: see under "Django app example" at https://mikebarkas.dev/2016/set-environment-variables-activating-virtualenv/
#  - however, with "venv", set in the "activate" file instead (not the activate.bat)
#    export SECRET_KEY='&ltc08quhgekn@2woi_62-fu@yfpp0$woj31x_@r^9e+hfl-o'
# - generate secret keys in python, >>> import secrets, >>> secrets.token_hex(24)

# About different shells and using venv (activate vs activate.bat, etc.): https://docs.python.org/3/library/venv.html


DEBUG = True
# DEBUG = (os.environ.get('DJANGO_DEBUG', "True") == "True") # -> if DJANGO_DEBUG is "True" ->  Boolean True (DEBUG must be set to a boolean)
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'paperratings_project',
#         'USER': 'funkykingston',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# Heroku: Update database configuration from $DATABASE_URL.
# import dj_database_url

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)


# or, from: https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python
# - DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True) 


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
# For production it is necessary to specify STATIC_ROOT, https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/
# - STATIC_ROOT - "The absolute path to the directory where collectstatic (python manage.py collectstatic) will collect static files for deployment." - https://docs.djangoproject.com/en/3.0/ref/settings/#static-files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# Heroku-specific information - DJANGO AND STATIC ASSETS (including the "whitenoise" package) - https://devcenter.heroku.com/articles/django-assets
# - Corey Schafer, "Deploy using Heroku": https://www.youtube.com/watch?v=6DI_7Zja8Zc&t=2691s


# During development, paths to static files are specified in STATIC_URL and STATICFILES_DIRS
STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage' # add 'whitenoise' package to requirements.txt, see e.g. https://www.youtube.com/watch?v=r0ECufCyyyw
# - ALSO DO: add to wsgi.py, from whitenoise.django import DjangoWhiteNoise, application = DjangoWhiteNoise(application)

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