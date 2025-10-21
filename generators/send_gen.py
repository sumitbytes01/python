def coffee_customer():
    print("""Welcome to the coffee shop!
                What coffee would you like?""")
    order = yield     
    while True:
        print(f"Preparing your {order}...")
        order = yield

stall = coffee_customer()
next(stall)  # Prime the generator
stall.send("cold brew") # resume the generator and send an order
stall.send("hot brew")
        