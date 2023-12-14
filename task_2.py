from app import cel
import time

@cel.task
def sub(x, y):
    print("sub start")
    time.sleep(1)
    return x - y