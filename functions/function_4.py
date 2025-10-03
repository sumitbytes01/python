def calulate_bills(cups, price_per_cup=5):
    total = cups * price_per_cup
    tax = total * 0.07
    return total + tax

my_bill = calulate_bills(3)
print(f"Total bill (including tax): ${my_bill:.2f}")
