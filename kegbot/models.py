from django.conf import settings
from django.db import models


class Beverage(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.FloatField(null=True, blank=True)
    ibu = models.IntegerField(null=True, blank=True)
    srm = models.IntegerField(null=True, blank=True)


class Tap(models.Model):
    channel = models.CharField(max_length=10)
    factor = models.IntegerField(default=1)
    total_volume = models.FloatField(default=0)
    beverage = models.ForeignKey(Beverage, null=True, blank=True)
    current_volume = models.FloatField(default=0)

    def reset_volume(self):
        self.current_volume == self.total_volume

    def dispense(self, pulses):
        self.current_volume = (self.current_volume or 0) - (pulses / self.factor)


class TapReader:
    def __init__(self, tap):
        self.tap = tap
        self.pulses = 0
        settings.BOARD.setup_event_handling(self.tap.channel, self.process_pulse)

    def reset_pulses(self):
        self.pulses = 0

    def process_pulse(self, *args):
        self.pulses += 1

    def update_volume(self):
        if self.pulses:
            self.tap.dispense(self.pulses)
            self.reset_pulses()
            return True
        return False

