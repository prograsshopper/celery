# celery 시작하는 entrypoint
from celery import Celery

# 첫번째 방법: 직접 지정
app = Celery(
    'worker',
    broker='redis://redis:6379/0', backend='redis://redis:6379/0', include=['worker.tasks']
)

# 두번째 방법: celeryconfig파일의 내용을 사용하는 방법
# app = Celery('worker', include=['worker.tasks'])
# app.config_from_object('celeryconfig')

app.conf.task_routes = {
    'worker.tasks.add': {
        'queue': 'queue2'
    },
    'worker.tasks.mul': {
        'queue': 'queue2'
    },
    'worker.tasks.xsum': {
        'queue': 'queue2'
    },
}

if __name__ == '__main__':
    app.start()
