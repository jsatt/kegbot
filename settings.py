import sys

from kegbot.settings import *  # noqa

BOARD = {
    'BACKEND': 'kegbot.boards.dev',
}
DEBUG = True


# Celery Settings

BROKER_URL = 'django://'
INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',

    'kombu.transport.django',
)
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# My Settings
INSTALLED_APPS += ('django_extensions',)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(process)d] %(levelname)-8s %(name)s: %(message)s'  # noqa
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'default'
        },
    },
    'loggers': {
        'kegbot': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
