# dictionary, named indexing
dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict2 = dict(name='Bob', age=25, city='Los Angeles')
print(dict1['name'])  # Output: Alice

print(dict1) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
del dict1['age']
print(dict1)  # Output: {'name': 'Alice', 'city': 'New  York'}

keys = dict2.keys()
values = dict2.values()
items = dict2.items()
print(keys)    # Output: dict_keys(['name', 'age', 'city'])
print(values)  # Output: dict_values(['Bob', 25, 'Los Angeles'])
print(items)   # Output: dict_items([('name', 'Bob'), ('age',

print(dict1)      # Output: {'name': 'Alice', 'city': 'New York'}
last_item = dict1.popitem()
print(last_item)  # Output: ('city', 'New York')
print(dict1)      # Output: {'name': 'Alice'}

print(dict1.get("note"))