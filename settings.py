import sys

from kegbot.settings import *  # noqa

BOARD = {
    'BACKEND': 'kegbot.boards.dev',
}
DEBUG = True


# Celery Settings

BROKER_URL = 'django://'
INSTALLED_APPS += ('kombu.transport.django',)


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
