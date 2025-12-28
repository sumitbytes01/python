# [expression for item in oterable if conditions]

coffee_menu = ["cold brew","devil's cold brew","espresso","latte","cappuccino","mocha"]

cold_brews = [coffee for coffee in coffee_menu if "cold" in coffee]
print(cold_brews)

hot_brews = [coffee for coffee in coffee_menu if "cold" not in coffee]
print(hot_brews)

long_name_brew = [coffee for coffee in coffee_menu if len(coffee) > 6]

for name in long_name_brew:
    print(name, len(name))