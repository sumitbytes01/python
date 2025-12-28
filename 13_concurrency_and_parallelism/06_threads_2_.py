import threading
import time

def prepare_coffee(type, wait_time):
    print(f"started {type} coffee brewing...")
    time.sleep(wait_time)
    print(f"completed {type} coffee brewing...")

t1 = threading.Thread(target=prepare_coffee, args=("mocha", 2))
t2 = threading.Thread(target=prepare_coffee, args=("cappaccino", 2))

t1.start()
t2.start()

t1.join()
t2.join()