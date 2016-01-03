from RPi import GPIO

from .base import BaseBoard


class Board(BaseBoard):
    def __init__(self, mode=None):
        self.gpio = GPIO
        modes = {
            'BCM': GPIO.BCM,
            'BOARD': GPIO.BOARD,
        }
        self.mode = modes.get(mode, GPIO.BOARD)
        GPIO.setmode(self.mode)

    def setup_event_handling(self, channel, callback):
        self.gpio.setup(channel, self.gpio.IN, pull_up_down=self.gpio.PUD_UP)
        self.gpio.add_event_detect(
            channel, self.gpio.RISING, callback=callback, bouncetime=20)

    def teardown_event_handling(self, channel):
        self.gpio.remove_event_detect(channel)
