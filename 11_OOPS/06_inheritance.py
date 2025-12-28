class BaseCoffee:
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type

    def prepare(self):
        return f"Preparing a cup of {self.coffee_type} coffee."

class SpecialtyCoffee(BaseCoffee):
    def add_spices(self):
        return "Adding special spices."
    
# lets see how composition works
class CoffeeWithSpices():
    coffee_cls = BaseCoffee # composition
    
    def __init__(self):
        self.coffee = self.coffee_cls("Regular")

    def serve(self):
        print(f"serving {self.coffee.coffee_type} coffee")
        return self.coffee.prepare()

class FancyCoffeeShop(CoffeeWithSpices):
    coffee_cls = SpecialtyCoffee

special_coffee = SpecialtyCoffee("Special")
print(special_coffee.add_spices())
print(special_coffee.prepare())

print("-------------------------")

coffee_with_spices = CoffeeWithSpices()
print(coffee_with_spices.serve())

print("-------------------------")

fancy_shop = FancyCoffeeShop()
print(fancy_shop.serve())
print(fancy_shop.coffee.add_spices())  # Accessing method from SpecialtyCoffee

