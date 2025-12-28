def update_order():
    coffee_type = "vanilla"
    def kitchen():
        nonlocal coffee_type # non-local looks in the first outer function
        coffee_type = "hot-coffee"
    kitchen()
    print(f"Coffee type is: {coffee_type}")

update_order()

