def infinite_coffee():
    """Generate an infinite sequence of coffee names."""
    coffees = ["cold brew", "devil's cold brew"]
    index = 0
    while True:
        yield coffees[index % len(coffees)]
        index += 1

stall = infinite_coffee()
for _ in range(10):
    print(next(stall))