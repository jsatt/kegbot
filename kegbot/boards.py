class Board:
    def setup_event_handling(self, channel, callback):
        raise NotImplementedError

    def teardown_event_handling(self, channel):
        pass


class RasperryPi(Board):
    def __init__(self, mode=None):
        from RPi import GPIO
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


from random import randrange
from time import sleep
import threading


class DevelopementBoard(Board):
    def __init__(self):
        self.threads = []

    def setup_event_handling(self, channel, callback):
        thread = threading.Thread(target=self._fake_pulse, args=(callback,))
        thread.setDaemon(True)
        thread.start()
        self.threads.append(thread)

    def teardown_event_handling(self, channel):
        for thread in self.threads:
            thread.cancel()

        self.threads.clear()

    def _fake_pulse(self, callback):
        while True:
            callback()
            sleep(randrange(1, 8) / 10)
