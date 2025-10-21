def local_coffee_shop():
    yield "cold brew"
    yield "devil's cold brew"

def global_coffee_shop():
    yield "mocha"
    yield "espresso"

def full_coffee_shop():
    yield from local_coffee_shop()
    yield from global_coffee_shop()

for coffee in full_coffee_shop():
    print(coffee)

print("\n")

def coffee_stall():
    try:
        while True:
            order = yield "waiting for coffee order"
    except:
        print("Closing shop, no more orders.")

stall = coffee_stall()
print(next(stall))  # Prime the generator
stall.throw(Exception)  # Close the shop by throwing an exception
# or you can use stall.close() to close the generator. cleanup