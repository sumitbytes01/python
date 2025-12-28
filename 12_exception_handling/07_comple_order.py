class InvalidCoffeeException(Exception):
    pass

def bill(flavour, cups):
    menu = {"espresso":10, "cold-coffee":20}
    try:
        if flavour not in menu:
            raise InvalidCoffeeException(f"Flavou {flavour} not in menu !!!")
        if not isinstance(cups, (int, float)):
            raise TypeError("Cups is not a number")
        total = menu[flavour] * cups
        print(f"Total bill for {flavour} coffee {cups} cups is : {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting our coffee shop")

bill("espresso", 20)
print("-------------")
bill("espresso", "20e")
print("-------------")
bill("mocha", "20e")



