import threading
import time

def boil_milk():
    print("Bioling milk...")
    time.sleep(2)
    print("Milk boiled")

def toast_bun():
    print("toasting bun")
    time.sleep(3)
    print("done with toasting bun")

boil_milk()
toast_bun()

start = time.time()

thread1 = threading.Thread(target=boil_milk)
thread2 = threading.Thread(target=toast_bun)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"time taken for boiling milk and toasting bun is {end - start}")
print("Program executed successfully...")