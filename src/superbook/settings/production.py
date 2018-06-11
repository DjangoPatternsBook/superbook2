# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
from .base import *             # NOQA

# import dj_database_url
# from decouple import config, Csv

# # For security and performance reasons, DEBUG is off by changeable
# SECRET_KEY = config('SECRET_KEY', default="not-a-secret")
# DEBUG = config('DEBUG', default=False, cast=bool)
# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL'))
# }
# DATABASES['default']['CONN_MAX_AGE'] = 500
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# TEMPLATE_DEBUG = DEBUG

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import os
DEBUG = os.environ.get('DEBUG', False)

WSGI_APPLICATION = 'src.superbook.wsgi.application'

# Logging
import logging.config
from django.utils.log import DEFAULT_LOGGING

# Disable Django's logging setup
LOGGING_CONFIG = None

LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': 'WARNING',
            'handlers': ['console', ],
        },
        # Our application code
        'app': {
            'level': LOGLEVEL,
            'handlers': ['console', ],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        # Default runserver request logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
    },
})

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
