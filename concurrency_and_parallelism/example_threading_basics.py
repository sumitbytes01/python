# concurrency: switching between the tasks. Do a task for a finite amount of time, switch to another task, switch back to another task.
# Parallelism: doing multiple tasks simultaneously. Can be performed on CPUs having multiple cores.
# there are cons and pros of both. It depends on you use case.

import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"taking orders for: {i}")
        #Partially, yes — sleep() appears to control coordination, but it’s not a reliable coordination mechanism.
        time.sleep(1)

def brew_coffee():
    for i in range(1, 4):
        print(f"Brewing coffee for: {i}")
        time.sleep(2)

# create threads
take_orders = threading.Thread(target=take_orders)
brew_coffee = threading.Thread(target=brew_coffee)

# invoke threads
take_orders.start()
brew_coffee.start()

# wait for both to finish
# The join() method in Python threading is used to make one thread wait for another thread to complete before 
# continuing execution. When you call thread.join() on a thread object, the calling thread (often the main thread) is 
# blocked until the thread on which join was called finishes its job.
# In practical terms, join() ensures that a thread completes before the program proceeds further.
take_orders.join()
brew_coffee.join()

print(f"Orders taken, coffee brewed")
#In your example, the short sleeps inside each loop (1 second for taking orders, 2 seconds for brewing) 
# make their outputs feel coordinated because the delay intervals happen to align. During time.sleep(), 
# that particular thread yields control to the OS scheduler (the Global Interpreter Lock is released),
# so the other thread can run

# But real coordination or synchronization between threads should use Locks, Events, Conditions, or 
# Queues from the threading module — not sleep().