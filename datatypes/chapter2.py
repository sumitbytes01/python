student_names=set()
print(f"intial student names:{id(student_names)}")
print(f"intial student names:{student_names}")
# since list is mutable type it cannot be added to set and thi will fail
# greet = [123,123,123,123,123]
# the following will pass:
greet = (123,123,123,123,123)
student_names.add("Alice")
student_names.add("Sumit")
student_names.add("Sumit")
student_names.add(greet)
print(f"after student names: {id(student_names)}")
print(f"after student names: {student_names}")