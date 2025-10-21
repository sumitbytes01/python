chai_size = input(f"Enter the cup size: ").lower()

if chai_size in ("small", "medium", "large"):
    print(f"Size input is correct")

price = 0

if chai_size=="small":
    price= 10
elif chai_size=="medium":
    price= 15
elif chai_size == "large":
    price= 20
else:
    print("Unknown Cup Size")

print(f"Chai Size is: {chai_size} and price is: {price}")