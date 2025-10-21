class Coffee:
    temperature = "hot"
    flavor = "vanilla"
    strong = "mild"

real_coffee = Coffee()
print(f"real coffee: {real_coffee.temperature}")  # Accessing class variable through an object
real_coffee.temperature = "cold"
print(f"real coffee after changing temperature: {real_coffee.temperature}")  # Accessing instance variable
print(f"Coffee class temperature: {Coffee.temperature}")  # Class variable remains unchanged

del real_coffee.temperature  # Deleting instance variable
print(f"real coffee after deleting instance variable: {real_coffee.temperature}")  # Accessing class variable again

real_coffee.sugar = "2 spoons"  # Adding an instance variable
print(f"real coffee sugar: {real_coffee.sugar}")  # Accessing instance
del real_coffee.sugar  # Deleting instance variable
print(f"real coffee sugar after deleting instance variable: {getattr(real_coffee, 'sugar', "i think its deleted")}")
