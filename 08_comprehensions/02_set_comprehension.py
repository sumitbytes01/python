coffee_menu = ["cold brew",
               "devil's cold brew",
               "espresso",
               "latte",
               "cappuccino",
               "mocha",
               "espresso",
               "latte"]

for item in coffee_menu:
    print(item)
    
unique_coffee = {coffee for coffee in coffee_menu}
print(unique_coffee)

long_name_coffee = {coffee for coffee in coffee_menu if len(coffee) > 10}
print("long_name_coffee: ", long_name_coffee)

coffee_ingredients = {"black coffee": ["water","coffee beans"],
                        "latte": ["espresso","steamed milk"],
                        "cappuccino": ["espresso","steamed milk","foam"],
                        "mocha": ["espresso","steamed milk","chocolate","whipped cream"]
                    }

# using {} instead of [] creates a set comprehension
unique_coffee_ingredients = {ingredient 
                             for ingredients in coffee_ingredients.values() 
                             for ingredient in ingredients}
all_coffee_ingredients = [ingredient for ingredients_list in coffee_ingredients.values() for ingredient in ingredients_list]
print(f"all values:{all_coffee_ingredients}")
print(f"unique values:{unique_coffee_ingredients}")

