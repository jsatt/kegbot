import logging

import arrow

from .boards import board
from .models import Tap

logger = logging.getLogger(__name__)


class TapReader:
    def __init__(self, tap):
        self.tap = tap
        self.pulses = 0
        self.first_pulse = None
        self.last_pulse = None
        board.setup_event_handling(self.tap.channel, self.process_pulse)

    @classmethod
    def get_readers(cls):
        taps = Tap.objects.all()
        return [TapReader(t) for t in taps]

    def reset_pulses(self):
        self.pulses = 0
        self.first_pulse = None
        self.last_pulse = None

    def process_pulse(self, *args):
        self.pulses += 1
        now = arrow.now()
        if not self.first_pulse:
            self.first_pulse = now
        self.last_pulse = now

    def as_payload(self):
        return {
            'tap': self.tap.id,
            'first_pulse': self.first_pulse.datetime,
            'last_pulse': self.last_pulse.datetime,
            'pulses': self.pulses,
        }
