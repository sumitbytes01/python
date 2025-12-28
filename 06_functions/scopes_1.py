def serve_coffee():
    coffee_type = "espresso"
    print(f"Serving a cup of {coffee_type}")

coffee_type = "latte"

serve_coffee()  # Output: Serving a cup of espresso
print(f"outside function: {coffee_type}")

print("--------------------------------------------")

def coffee_counter():
    coffee_order = "cappuccino"
    def take_order():
        coffee_order = "flat white"
        print(f"inner: {coffee_order}")
    take_order()
    print(f"outer: {coffee_order}")
coffee_order = "americano"
coffee_counter()
print(f"outside function(Global): {coffee_order}")