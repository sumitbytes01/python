daily_sales = [100, 200, 300]

total_cups = (sale for sale in daily_sales if sale >= 150)
print(total_cups)

# memory efficient code

total_cups = sum(sale for sale in daily_sales if sale >= 150)
print(total_cups)