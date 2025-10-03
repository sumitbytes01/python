def update_order():
    coffee_type = "mocha"
    def change_order():
        nonlocal coffee_type
        coffee_type = "macchiato"
        print(f"inner: {coffee_type}")
    change_order()
    print(f"outer: {coffee_type}")

update_order()