from app import cel
import time

@cel.task
def add(x, y):
    print("add start")
    time.sleep(1)
    return x + y


@cel.task
def my_task():
    print("---Executing my timed task...")
    return 2.5