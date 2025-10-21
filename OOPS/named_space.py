class SimpleCoffee:
    origin = "India"

print(SimpleCoffee.origin)  # Accessing class variable without creating an object

SimpleCoffee.is_hot = True  # Dynamically adding a class variable
print(SimpleCoffee.is_hot)

# creating objects from class

cappuccino = SimpleCoffee()
print(type(cappuccino))
print(cappuccino.origin)  # Accessing class variable through an object
print(cappuccino.is_hot)  # Accessing dynamically added class variable through an object
cappuccino.is_hot = False  # Adding an instance variable
print(f"cappuccino is hot?:{cappuccino.is_hot}") # Accessing instance variable
print(f"SimpleCoffee is hot?:{SimpleCoffee.is_hot}")  # Class variable remains unchanged

cappuccino.flavor = "Caramel"  # Adding another instance variable
print(f"cappuccino flavor:{cappuccino.flavor}")
print(f"SimpleCoffee flavor:{getattr(SimpleCoffee, 'flavor', 'Not Found')}")  # Accessing non-existent class variable
#GitHub Copilot
# getattr(obj, name[, default]) looks up an attribute by name (string) on obj:

# Returns the attribute value if it exists.
# If the attribute is missing and default is provided, returns default.
# If missing and no default, raises AttributeError.