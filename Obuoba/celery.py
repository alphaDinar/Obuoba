import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Obuoba.settings')
app = Celery('Obuoba')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'UTC'
 
app.conf.beat_schedule = {
    "add_first": {
        "task": "app.tasks.task_name",
        "schedule": timedelta(hours=1),
    },
}
 
app.autodiscover_tasks()