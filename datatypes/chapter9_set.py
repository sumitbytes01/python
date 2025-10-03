#set
essential_names = {"Alice", "Bob", "Charlie"}
optional_names = {"David", "Eve", "Frank", "Bob"}

all_names = essential_names | optional_names
print(f"all names: {all_names}, type: {type(all_names)}")

common_names = essential_names & optional_names
print(f"common_names: {common_names}, type: {type(common_names)}")

print(f"is Alice in essential names: {'Alice' in essential_names}")
print(f"is Sumit in essential names: {'Sumit' in essential_names}")

only_in_common = essential_names - optional_names
print(f"only in essential names: {only_in_common}, type: {type(only_in_common)}")
only_in_optional = optional_names - essential_names
print(f"only in optional names: {only_in_optional}, type: {type(only_in_optional)}")
 
# immutable set
frozenset_names = frozenset(["Grace", "Heidi", "Ivan"])
print(f"frozenset names: {frozenset_names}, type: {type(frozenset_names)}")

frozenset_names.add("Judy")  # This will raise an AttributeError as frozensets are immutable
print(f"frozenset names after add: {frozenset_names}")