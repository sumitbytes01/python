coffee_prices = {"cold brew": 3.00,
                 "devil's cold brew": 4.00,
                 "espresso": 2.50,
                 "latte": 4.50}

coffee_price_in_dollars = {coffee: f"{price/80}$" for coffee, price in coffee_prices.items()}

print(coffee_price_in_dollars)