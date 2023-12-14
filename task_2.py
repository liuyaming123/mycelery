from app import cel
import time

@cel.task()
def add_2(x, y):
    print("add_2 start")
    time.sleep(1)
    return x + y