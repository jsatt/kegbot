from django.db import models
from django.utils import timezone


class Beverage(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    abv = models.FloatField(null=True, blank=True)
    ibu = models.IntegerField(null=True, blank=True)
    srm = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tap(models.Model):
    channel = models.CharField(max_length=10)
    pulses_per_ml = models.IntegerField(default=1)
    total_ml = models.FloatField(default=0)
    dispensed_ml = models.FloatField(default=0)
    beverage = models.ForeignKey(Beverage, null=True, blank=True)

    def __str__(self):
        return self.channel or str(self.pk)

    def reset_dispense(self):
        self.dispensed_ml = 0

    def calculate_ml(self, pulses):
        return pulses / self.pulses_per_ml


class Pour(models.Model):
    tap = models.ForeignKey(Tap, related_name='pours')
    beverage = models.ForeignKey(Beverage, blank=True, null=True, related_name='pours')
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)
    dispensed_ml = models.FloatField(default=0)

    def __str__(self):
        return '{} - tap {} - {}'.format(
            self.beverage,
            self.tap,
            self.start
        )
