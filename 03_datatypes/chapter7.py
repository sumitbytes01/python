#tuples - immutable
student_names = ("Alice", "Bob", "Charlie")
print(f"student names: {student_names}, type: {type(student_names)}")

name1, name2, name3 = student_names
print(f"name1: {name1}, name2: {name2}, name3:{name3}")

Alice_marks, Bob_marks, Charlie_marks = 85, 90, 95
print(f"Alice_marks: {Alice_marks}, Bob_marks: {Bob_marks}, Charlie_marks: {Charlie_marks}")

#swap marks of Alice and Bob
Alice_marks, Bob_marks = Bob_marks, Alice_marks
print(f"after swap Alice_marks: {Alice_marks}, Bob_marks: {Bob_marks}")

# using in
print(f"is Alice in student names: {'Alice' in student_names}")
print(f"is Sumit in student names: {'Sumit' in student_names}")

student_names.__add__("Sumit")  # this will not work as tuples are immutable
print(f"is Sumit in student names: {'Sumit' in student_names}")