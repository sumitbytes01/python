coffee_type = "latte"

def front_desk():
    coffee_type = "espresso"
    def barista():
        global coffee_type
        coffee_type = "cappuccino"
        print(f"Barista prepared: {coffee_type}")
    barista()
    print(f"Serving a cup of {coffee_type}")

front_desk()  # Output: Serving a cup of espresso
print(f"Outside function: {coffee_type}")
