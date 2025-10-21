# sets are mutable, since we can change the value
student_names=set()
print(f"intial student names id:{id(student_names)}")
print(f"intial student names:{student_names}")
# since list is mutable type it cannot be added to set and this will fail
# greet = [123,123,123,123,123]
# the following will pass: as it is tuple and immutable
greet = (123,123,123,123,123)
student_names.add("Alice")
student_names.add("Sumit")
student_names.add("Sumit")
student_names.add(greet)
print(f"after student names id: {id(student_names)}")
print(f"after student names: {student_names}")