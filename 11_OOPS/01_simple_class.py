class Coffee:
    pass

class CoffeeTime:
    pass

print(type(Coffee))

espresso = Coffee()
mocha = Coffee()

print(type(espresso))
print(type(espresso) is Coffee)
print(type(espresso) is CoffeeTime)