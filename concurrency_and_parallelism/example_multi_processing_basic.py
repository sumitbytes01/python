from multiprocessing import Process
from time import sleep

def brew_coffee(name):
    print(f"Start brewing: {name}")
    sleep(3)
    print(f"Finished brewing: {name}")

if __name__ == "__main__":
    coffee_makers = [Process(target= brew_coffee, args = (f"coffee maker: {i+1}", )) for i in range(3)]

    # start of process
    for p in coffee_makers:
        p.start()

    # wait for all
    for p in coffee_makers:
        p.join()

    print("All coffee served")

