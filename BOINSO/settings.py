"""
Django settings for BOINSO project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '23(uav*@6m&$fg3ld@@nstgax%g8(7gi=4@&kqa(dd=rg8)$2o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# I don't use the admin views as I have the browsable api
# If you want to use it you cann add the support here
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'oauth2_provider',
    'rest_framework',
    'core',
    'api'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'BOINSO.urls'

WSGI_APPLICATION = 'BOINSO.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# dev settings vor vagrant WalternativE/django_base_box postgres instance
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# this is just for travis tests
if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travisci',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Add your corresponding timezone here
# For development as I am in Austria I choose Europe/Vienna
TIME_ZONE = 'Europe/Vienna'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# template directories
# TEMPLATE_DIRS = (
#     BASE_DIR + '/templates',
# )

# config for OAuth2Provider
OAUTH2_PROVIDER = {
    # available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}


# beware if you plan to use standard permission methods here
# in some cases (as with the api_root method) this breaks
# the public access (as no user is deliverd)
REST_FRAMEWORK = {
    # I normally supply testdata in json format
    # as I tend to use the same fixtures in the front end
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#     'localhost',
# )

STATIC_ROOT = os.path.join(BASE_DIR, './staticfiles/')