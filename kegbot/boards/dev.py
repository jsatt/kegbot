from random import randrange
from time import sleep
import threading

from .base import BaseBoard


class Board(BaseBoard):
    """
    This is a board class intended for use during development process on a machine that
    may not have the GPIO API that is provided by Raspberry Pi, Edison and similar boards.

    Fake pulse events are generated at random intervals ranging from 100 to 800 milliseconds
    to insure that a change is happening regularly.
    """

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
