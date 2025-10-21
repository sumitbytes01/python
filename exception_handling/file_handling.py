file = open("file.txt", "w")
try:
    file.write("Espresso coffee - 2 cups")
finally:
    file.close

# new way
# auto close of file
with open("order.txt", "w") as file:
    file.write("Cold coffee - 4 cups")
    
# file.__enter__()
# file.__exit__()


