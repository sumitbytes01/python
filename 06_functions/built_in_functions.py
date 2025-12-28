def coffee_flavour(flavour="espresso"):
    """Function to return the coffee flavour.""" # This is a docstring, and should be the first line in the function
    return flavour

print(coffee_flavour.__doc__) # return docstring
print(coffee_flavour.__name__) # return function name

def generate_bill(coffee=0, samosa=0):
    """Function to generate the bill.
    :param coffee: number of coffee cups (each cup costs 10)
    :param samosa: number of samosas (each samosa costs 20)
    :return total amount"""
    total = coffee * 10 + samosa * 20
    return total

print("Thankyou!!!",generate_bill(2,1))