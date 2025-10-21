def serve_coffee():
    yield "Here's your coffee!"
    yield "Enjoy your coffee!"
    yield "Don't forget to tip your barista!"

stall = serve_coffee()
print(stall)

for cup in stall:
    print(cup)

print("--------------------------------" \
"----------------")

def get_coffee_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

def get_coffee_list():
    return ["cup1", "cup2", "cup3"]

gen = get_coffee_gen()
lst = get_coffee_list()
print(next(gen))
print(next(gen))
print(next(gen))
print(lst)