from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers

from .views import TapViewSet

router = routers.DefaultRouter()
router.register(r'taps', TapViewSet)

urlpatterns = (
    url(r'^api/', include(router.urls)),
)

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    urlpatterns += (
        url(r'^admin/', include(admin.site.urls)),
    )

# All other urls fallback to SPA
urlpatterns += (
    url(r'', TemplateView.as_view(template_name='index.html')),
)
