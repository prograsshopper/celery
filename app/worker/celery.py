import os

from django.conf import settings

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('worker') # celery initialize에 필요

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# celery 전용 constant 만들때 사용
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    task_routes = {
        'worker.tasks.dumb': {
            'queue': 'queue1'
        },
        'worker.tasks.add': {
            'queue': 'queue2'
        }
    }
)

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')