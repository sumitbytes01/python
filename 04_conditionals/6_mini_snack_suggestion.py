snack = input("Enter your snack here:").lower()
print(f"user said: {snack}")

if snack == "samosa" or snack == "kulfi":
    print(f"you ordered a nice snack")
else:
    print(f"Make a good choice of snack the next time")