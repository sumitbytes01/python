# number = 13
# remainder = number % 5

# if remainder:
#     print(f"{number} is not divisible by 5, remainder is {remainder}")

number = 13

if (remainder := number % 5):
    print(f"{number} is not divisible by 5, remainder is {remainder}")

# Using the walrus operator to assign and check in one line


available_sizes = ["S", "M", "L", "XL"]

if (size := input("Enter the size")) in available_sizes:
    print(f"Size {size} is available")
else:
    print(f"Size {size} is not available")


flavours = ["vanilla", "chocolate", "strawberry", "butterscotch"]
print(f"Available flavours are:{flavours}")

while (flavour := input("Which flavour do you want? ")) not in flavours:
    print(f"Sorry, we don't have {flavour}. Please choose from the available flavours")

print(f"Here is your {flavour} ice cream!")