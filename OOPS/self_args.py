class CoffeeCup:
    size = 150 #ml

    def describe(self):
        return f"This is a {self.size}ml cup of coffee"
    
my_coffee = CoffeeCup()
print(my_coffee.describe())  # Implicitly passes 'my_coffee' as '
print(CoffeeCup.describe(my_coffee))  # Explicitly passing the instance

my_coffee_cup2 = CoffeeCup() 
my_coffee_cup2.size = 300
print(my_coffee_cup2.describe())  # Uses the updated size for this instance
print(CoffeeCup.describe(my_coffee))  # Explicitly passing the instance