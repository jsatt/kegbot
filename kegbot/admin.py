from django.contrib.admin import site

from kegbot.models import (
    Beverage,
    Pour,
    Tap,
)

site.register(Beverage)
site.register(Pour)
site.register(Tap)
