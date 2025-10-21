def process_order(item, quantity):
    try:
        price = {"espresso": 20}[item]
        if not isinstance(quantity, (int, float)):
            raise TypeError
        cost = price * quantity
        print(f"Cost is {cost}")
    except KeyError:
        print("Sorry the coffee is not in the menu")
    except TypeError:
        print("Quantity must be a number")

process_order("espresso", 2)

process_order("espresso", "two")