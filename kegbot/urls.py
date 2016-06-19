from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import TapViewSet

router = routers.DefaultRouter()
router.register(r'taps', TapViewSet)

urlpatterns = (
    url(r'^api/', include(router.urls)),
)
