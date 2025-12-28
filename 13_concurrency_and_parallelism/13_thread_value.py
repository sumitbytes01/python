from multiprocessing import Value
import threading

def prepare_coffee(counter):
    for _ in range(100000):
        #with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    threads = [threading.Thread(target=prepare_coffee, args=(counter, ))for _ in range(3)]
    
    [t.start() for t in threads]
    [t.join() for t in threads]
    
    print("final counter value: ", counter.value)

