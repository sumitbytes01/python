# input params
def make_coffee(coffee, milk, sugar):
    print(coffee, milk, sugar)

make_coffee("Vanilla", "Yes", "No") # positional
make_coffee(coffee="Vanilla", milk="Yes", sugar="No") # keywords

def special_coffee()