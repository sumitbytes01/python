# In Python, a for-else loop is a special construct 
# where the else block runs only if the for loop 
# completes normally 
# (i.e., not interrupted by a break statement).
staff = [("John", 16), ("zoe", 21), ("Alice", 19)]
print(type(staff))
for name, age in staff:
    if age > 16:#22
        print(f"{name} is eligible for a senior position.")
        break
# fallback
else:
    print("No staff member is eligible for a senior position.")