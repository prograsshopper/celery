import time

from celery import shared_task
from celery.signals import task_prerun, task_postrun


@shared_task(queue='celery', rate_limit='1/m')  # limit rate
def add(x, y):
    return x + y


@shared_task
def dumb():
    return

@shared_task(queue='celery')
def xsum(numbers):
    return sum(numbers)


@shared_task(queue='celery')
def p1():
    time.sleep(5)
    return


@shared_task(queue='celery:1')
def p2():
    time.sleep(5)
    return


@shared_task(queue='celery:2')
def p3():
    time.sleep(5)
    return


@shared_task(queue='celery')
def print_result(x, y, msg=None):
    total = x + y
    if msg:
        return f"{msg}: {total}"
    return total
#  print_result.apply_async(args=[1, 2], kwargs={"msg": "The result is"})


@shared_task(queue='celery')
def sleep_task():
    time.sleep(10)
    return


def sync_task():
    result = sleep_task.apply_async()
    print("Waiting...")
    print(result.get()) # execution 기다려봄


def async_task():
    result = sleep_task.apply_async()
    print("Not Waiting...")
    print(result.task_id()) # 기다릴 필요 X

# signal
# Define signal handlers


@task_prerun.connect
def task_prerun_handler(sender, task_id, task, args, kwargs, **kwargs_extra):
    print(f"Task {task_id} is about to run: {task.name} with args {args}")


@task_postrun.connect
def task_postrun_handler(sender, task_id, task, args, kwargs, retval, state, **kwargs_extra):
    print(f"Task {task_id} has completed : {task.name} with result {retval}")


# simulate signal
def simulating_task_signal():
    # Call the celery task asynchronously
    result = add.delay(2, 3)

    # Get the result of the task
    final_result = result.get()
    print("Final Result: ", final_result)
