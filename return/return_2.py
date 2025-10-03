def return_coffee(order):
    if order == 0:
        return "espresso"
    elif order == 1:
        return "latte"
    return "cappuccino"
    print("I am done")

coffee = return_coffee(1)
print(coffee)  # Output: latte
print(return_coffee(0))  # Output: espresso
print(return_coffee(5))  # Output: cappuccino
print(return_coffee(2))  # Output: cappuccino

def pay_bill():
    return 5.0, 2.5 ,11 # amount, tip

amount, tip,_ = pay_bill()
print(f"Amount: {amount}, Tip: {tip}")