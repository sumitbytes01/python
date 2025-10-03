import recipes.flaours as flaours

print(flaours.latte_coffee())
print(flaours.cappuccino_coffee())

from recipes.flaours import latte_coffee, cappuccino_coffee
print(latte_coffee())
print(cappuccino_coffee())

# from .recipes.flaours import latte_coffee
# print(latte_coffee())