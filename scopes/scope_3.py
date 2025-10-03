coffee = "cappuccino"

def prepare_coffee(order):
    print(f"Preparing a cup of {order}")

prepare_coffee(coffee)

coffee = ["espresso", "latte", "cappuccino"]

def edit_coffee(orders):
    orders[0] = "flat white"
    print(f"Inside function: {orders}")

edit_coffee(coffee)

def make_coffee(coffee, milk, sugar):
    print(f"Making coffee with {coffee}, {milk}, and {sugar}")

make_coffee("espresso", "whole milk", 2) #positional arguments
make_coffee(milk="almond milk", coffee="latte", sugar=1) #keyword arguments

def special_coffee(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_coffee("espresso", "vanilla", milk="oat milk", sugar=2)

def coffee_order(order=[]):
    order.append("espresso")
    print(f"Order: {order}")

coffee_order()  # Order: ['espresso']
coffee_order()  # Order: ['espresso', 'espresso']

def coffee_order(order=None):
    if order is None:
        order=[]
    print(f"Order: {order}")

coffee_order()  # Order: ['espresso']
coffee_order()  # Order: ['espresso', 'espresso']
