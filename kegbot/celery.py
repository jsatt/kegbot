import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.conf import settings

app = Celery('kegbot')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
