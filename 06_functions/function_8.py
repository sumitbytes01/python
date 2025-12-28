coffee_type = "Plain"

def update_front_desk():
    coffee_type = "cold-coffee"
    def kitchen():
        global coffee_type # use carefully
        coffee_type = "vanilla"
    kitchen()
    print(f"coffee is: {coffee_type}")

update_front_desk()
print(f"coffee is: {coffee_type}")