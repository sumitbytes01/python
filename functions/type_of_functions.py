def pure_coffee(cups):
    return cups * 10

total_coffee = pure_coffee(3)

# Impure function
# not recommended
def impure_coffee(cups):
    global total_coffee
    total_coffee  += cups

#Recursive function
def pour_coffee(cups):
    print(cups)
    if cups <= 0:
        return "No more cups to pour!"
    print("Pouring a cup of coffee...")
    return pour_coffee(cups - 1)

print(pour_coffee(3))

#Lambda function

coffee_type = ["espresso", "latte", "cappuccino", "flat white", "espresso", "mocha"," macchiato"]

strong_coffee = list(filter(lambda coffee: coffee == "espresso", coffee_type))
print(strong_coffee)

not_strong_coffee = list(filter(lambda coffee: coffee != "espresso", coffee_type))
print(not_strong_coffee)