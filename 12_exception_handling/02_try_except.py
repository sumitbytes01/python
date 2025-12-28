coffee_menu = {"espresso": 10, "mocha": 20}

coffee_menu["espresso"]
# coffee_menu["cold-coffee"] # KeyError: 'cold-coffee'

try:
    coffee_menu["cold-coffee"]
except:
    print("key you are trying to access is not available")