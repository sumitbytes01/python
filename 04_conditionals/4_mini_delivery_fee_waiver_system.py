order_amount = int(input("Enter order amount: "))
print(f"Type of order amount, type:{type(order_amount)}")

delivery_fees = 0
if order_amount>500:
    print("Delivery is free:)")
else:
    print("Delivery fee is 30$")
    delivery_fees = 30

delivery_fees = 0 if order_amount>500 else 30

print(f"Delivery fees: {delivery_fees}$")

