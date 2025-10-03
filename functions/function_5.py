def add_vat(amount, vat_rate=0.2):
    """Calculate the total amount including VAT."""
    return amount * (1 + vat_rate)


orders_amounts = [100, 250, 400]

for amount in orders_amounts:
    total_with_vat = add_vat(amount)
    print(f"Original: ${amount}, with VAT: ${total_with_vat:.2f}")

