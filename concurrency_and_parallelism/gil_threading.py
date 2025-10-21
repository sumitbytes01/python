# GIL - Global Interpreter Lock
import threading
import time

def brew_coffee():
    print(f"{threading.current_thread.__name__} started brewing....")
    count = 0
    for i in range(100_000_000):
        count = count+1
    print(f"{threading.current_thread.__name__} finished brewing....")

thread1 = threading.Thread(target=brew_coffee, name="barista")
thread2 = threading.Thread(target=brew_coffee, name="CCD")

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"Total time taken: {end - start} to finish")