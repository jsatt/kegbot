from time import sleep

from django.core.management.base import BaseCommand

from kegbot.models import Tap, TapReader


class Command(BaseCommand):
    def handle(self, *args, **opts):
        taps = Tap.objects.all()
        readers = {t: TapReader(t) for t in taps}

        while True:
            for tap in taps:
                if readers[tap].update_volume():
                    tap.save()
            sleep(1)
