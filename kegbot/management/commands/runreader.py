import logging

from time import sleep

from django.conf import settings
from django.core.management.base import BaseCommand
import arrow

from kegbot.reader import TapReader
from kegbot.tasks import record_pulses

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **opts):
        readers = TapReader.get_readers()

        while True:
            now = arrow.now()
            dispense_expire = now.replace(seconds=-settings.DISPENSE_EXPIRE)

            for reader in readers:
                if reader.first_pulse:
                    if reader.last_pulse and reader.last_pulse < dispense_expire:
                        logger.debug('reset pulses')
                        reader.reset_pulses()
                    else:
                        payload = reader.as_payload()
                        logger.debug('send payload {}'.format(payload))
                        record_pulses.delay(payload=payload)
            sleep(1)
