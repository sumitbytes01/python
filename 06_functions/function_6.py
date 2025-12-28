def serve_coffee():
    coffee_type = "Vanilla" # local scope
    print(f"Inside function {coffee_type}")

coffee_type = "espresso" # global scope
serve_coffee()
print(f"outside function {coffee_type}")

# nested functions
def coffee_counter():
    coffee_order = "mocha" # enclosing scope
    def print_order():
        coffee_order = "hot-coffee"
        print("Inner: ", coffee_order)
    print_order()
    print("Outer: ", coffee_order)

coffee_order = "cold-coffee" # Global scope
 
coffee_counter()
print(f"Global: {coffee_order}")

