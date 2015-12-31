from time import sleep
import logging
import sys

from RPi import GPIO

logger = logging.getLogger(__name__)
GPIO.setmode(GPIO.BCM)


class RPiReader:
    def __init__(self, channel):
        self.channel = channel
        self._clicks = 0
        self.setup_event_handling()

    def setup_event_handling(self):
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.channel, GPIO.RISING, callback=self.process_click, bouncetime=20)

    def process_click(self, channel):
        logger.debug('click on channel {}'.format(self.channel))
        self._clicks += 1

    def reset_count(self):
        logger.debug('resetting click count on for channel {}'.format(self.channel))
        self._clicks = 0

    def get_count(self):
        return self._clicks


def start_loop():
    logger.debug('starting loop')
    reader = RPiReader(22)
    db = {reader: {'ttl': 0}}

    while True:
        reader.reset_count()
        sleep(1)
        db[reader]['ttl'] += reader.get_count()

        logger.debug('total clicks: {}'.format(db[reader]['ttl']))


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    start_loop()
