from multiprocessing import Process, Queue

def prepare_coffee(queue):
    queue.put("Cold coffee is ready")

queue = Queue()

if __name__ == "__main__":
    p = Process(target= prepare_coffee, args=(queue, ))
    p.start()
    p.join()
    print(queue.get())

