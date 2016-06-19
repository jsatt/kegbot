from celery import shared_task
from django.db.models import Coalesce, F, functions

from .models import Pour, Tap


@shared_task
def record_pulses(payload):
    tap = Tap.objects.get(id=payload['tap'])
    pour, _ = Pour.objects.get_or_create(tap=tap, start=payload['first_pulse'])
    mls = tap.calculate_ml(payload['pulses'])
    dispensed_ml = F('dispensed_ml') + mls
    Pour.objects.filter(id=pour.id).update(
        beverage=tap.beverage,
        dispensed_ml=dispensed_ml,
        end=functions.Greatest(payload['last_pulse'], Coalesce('end', 'start'))
    )

    Tap.objects.filter(id=tap.id).update(dispensed_ml=dispensed_ml)
