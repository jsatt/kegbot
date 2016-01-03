from importlib import import_module

from django.conf import settings

board_settings = settings.BOARD.copy()
backend = board_settings.pop('BACKEND')

try:
    board_module = import_module(backend)
except ImportError:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured(
        'Please select the proper Board which kegbot is running on. Failing to confgure '
        'the correct board will cause Kegbot to run improperly and potentially damage '
        'your hardware.'
    )

board = board_module.Board(**board_settings)
