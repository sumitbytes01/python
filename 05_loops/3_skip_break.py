flavors = ["vanilla", "chocolate", "out of stock", "discontinued", "cookie dough"]

for flavor in flavors:
    if flavor == "out of stock":
        print(f"Skipping {flavor} flavor.")
        continue
    if flavor == "discontinued":
        print(f"Stopping the service as {flavor} flavor is discontinued.")
        break
    print(f"Serving {flavor} ice cream.")