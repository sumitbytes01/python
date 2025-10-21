class CoffeeOrder:
    def __init__(self, coffee_type_, size):
        self.coffee_type = coffee_type_
        self.size = size

    def summary(self):
        return f"You ordered a {self.size}ml cup of {self.coffee_type} coffee."
    
my_order = CoffeeOrder("latte", 250)
print(my_order.summary())  # Output: You ordered a 250ml cup of latte coffee