from rest_framework.viewsets import ModelViewSet

from .models import Tap
from .serializers import TapSerializer


class TapViewSet(ModelViewSet):
    queryset = Tap.objects.all()
    serializer_class = TapSerializer
