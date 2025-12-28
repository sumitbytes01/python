class OutOfIngredientsError(Exception):
    pass

def make_coffee(coffee, sugar):
    if coffee == 0 or sugar == 0:
        raise OutOfIngredientsError("I need coffee and Sugar to survive!!!")
    print("Coffee with Sugar is ready")

make_coffee(2, 1)

make_coffee(0, 1)