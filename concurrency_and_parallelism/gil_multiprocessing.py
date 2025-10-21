# GIL - Global Interpreter Lock - protect access to Python objects and avoid race conditions,
# because CPython's memory management is not fully thread-safe,
# Python’s GIL is more global and less flexible
# To summarize:

#The GIL is always active in a CPython process.

#You don’t need to provide anything like synchronized in Java to “enable” it.

#To avoid GIL limitations for CPU-bound work, Python developers often use multiprocessing (
# separate processes, each with its own Python interpreter and GIL) or C extensions that release the 
# GIL during heavy computations.​

#This automatic nature of the GIL is unique to Python’s CPython implementation and is a core reason why 
# Python threading is limited in true parallelism for CPU-bound tasks.
from multiprocessing import Process
import time

def crunch_numbers():
    print("starting the count process")
    count = 0
    for i in range(100_000_000):
        count = count+1
    print(f"ending the count process")

if __name__ == '__main__':

    p1 = Process(target=crunch_numbers, name="barista")
    p2 = Process(target=crunch_numbers, name="CCD")

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken: {end - start} to finish")
# Yes, Java can perform CPU-bound tasks faster than CPython Python due to its ability to 
# leverage multiple cores simultaneously, 
# while Python’s GIL restricts execution to a single thread at a time.​