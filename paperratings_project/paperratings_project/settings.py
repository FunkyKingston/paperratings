"""
For more information on this file, see: 
- https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see: 
- https://docs.djangoproject.com/en/3.1/ref/settings/
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
    # 'whitenoise.runserver_nostatic', # for using whitenoise during development (instead of the default 'django.contrib.staticfiles') - http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
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
    'whitenoise.middleware.WhiteNoiseMiddleware', # http://whitenoise.evans.io/en/stable/django.html (should/has to be placed directly after django.middleware.security.SecurityMiddleware)
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
# Static files (CSS, JavaScript, Fonts, Images, ...) #
######################################################
# *******************
# *** DEVELOPMENT *** (i.e. running locally, with Debug = True)
# *******************
# - Managing static files (e.g. images, JavaScript, CSS) - https://docs.djangoproject.com/en/3.1/howto/static-files/
#   - Using django.contrib.staticfiles works fine during development mode (DEBUG = True) however: 
#     "This method is grossly inefficient and probably insecure, so it is unsuitable for production.""
#     (- To use with DEBUG = False, need to force using --insecure flag https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#cmdoption-runserver-insecure )


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL to use when referring to static files located in STATIC_ROOT, e.g. http://127.0.0.1:8000/static/css/main.css
STATIC_URL = '/static/'

# Additional static files - those that aren't tied to any particular [django] app, but to the purely React-based /frontend subfolder - https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'static', 'frontend'),
]


# ******************
# *** PRODUCTION ***
# ******************
# - "Deploying static files" (not about [user-uploaded] media files) - https://docs.djangoproject.com/en/3.1/howto/static-files/deployment
# - "Django and Static Assets", to serve Media files on Heroku - https://devcenter.heroku.com/articles/django-assets

# -> "WhiteNoise - Radically simplified static file serving for Python web apps" - http://whitenoise.evans.io/en/stable/ , http://whitenoise.evans.io/en/stable/django.html

# Optional:
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # setting up STATICFILES_STORAGE with WhiteNoise


# For production it is necessary to specify STATIC_ROOT - https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/
# - STATIC_ROOT - "The absolute path to the directory where collectstatic (python manage.py collectstatic) will collect static files for deployment."
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



###############
# Media files #
############### 
# *******************
# *** DEVELOPMENT *** (i.e. running locally, with Debug = True)
# *******************
# where uploaded files will be stored on the file system
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # BASE_DIR set by django
# how we're going to access the media files in the browser
MEDIA_URL = '/media/'


# ******************
# *** PRODUCTION ***
# ******************
# Serving Media Files - WhiteNoise is not suitable for serving user-uploaded “media” files.
# - http://whitenoise.evans.io/en/stable/django.html#serving-media-files
#   - discussion involving the author of WhiteNoise (evansd) - https://github.com/evansd/whitenoise/issues/32

# - Corey Schafer - "Python Django Tutorial: Full-Featured Web App Part 13 - Using AWS S3 for File Uploads" - https://www.youtube.com/watch?v=kt3ZtW9MXhw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=16

# - "Serve Django Static and Media Files in Production" - https://medium.com/swlh/serve-django-static-and-media-files-in-production-348fe6c7781d




# - "Uploading images to REST API backend in React JS - https://coleruche.com/post/uploading-images-to-REST-API-backend-in-React-JS/











