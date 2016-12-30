from rest_framework.serializers import ModelSerializer

from .models import Tap


class TapSerializer(ModelSerializer):
    class Meta:
        model = Tap
        fields = (
            'id', 'channel', 'pulses_per_ml', 'current_level', 'total_ml',
            'dispensed_ml', 'beverage', 'pours',
        )
        depth = 1
