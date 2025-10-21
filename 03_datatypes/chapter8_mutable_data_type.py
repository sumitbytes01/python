# List (array) is a mutable data type in Python, meaning that its contents can be changed after 
# it is created. 
# Here are some key points about lists:
student_names = ["Alice", "Bob", "Charlie"]

student_names.append("Sumit")  # Adding an element to the end of the list

print(f"student names after append: {student_names}, type: {type(student_names)}")

poped_student = student_names.pop()  # Removing the last element from the list
print(f"poped student: {poped_student}")
print(f"student names after pop: {student_names}, type: {type(student_names)}")

student_names.remove("Alice")  # Removing a specific element from the list


print(f"student names after removing Alice: {student_names}, type: {type(student_names)}")

student_names_1 = ["David", "Eve"]
student_names_2 = ["Frank", "Grace"]

print(f"student names 1 before insert: {student_names_1}, type: {type(student_names_1)}")
student_names_1.insert(1, "Zara")  # Inserting an element at a specific index
print(f"student names 1 after insert: {student_names_1}, type: {type(student_names_1)}")   

print(f"student names 1 before reverse: {student_names_1}, type: {type(student_names_1)}")
student_names_1.reverse()
print(f"student names 1 after reverse: {student_names_1}, type: {type(student_names_1)}")

print(f"student names 1 before sort: {student_names_1}, type: {type(student_names_1)}")
student_names_1.sort()
print(f"student names 1 after sort: {student_names_1}, type: {type(student_names_1)}")

student_marks = [85, 90, 78, 92, 88]
print(f"student min marks: {min(student_marks)}")
print(f"student max marks: {max(student_marks)}")

# Operator Overloading
combined_student_names = student_names_1 + student_names_2  # Concatenation of two lists
print(f"combined student names: {combined_student_names}, type: {type(combined_student_names)}")

repeated_student_names = student_names_1 * 3  # Repeating the list
print(f"repeated student names: {repeated_student_names}, type: {type(repeated_student_names)}")

student_name = bytearray(b"Sumit")
student_name = student_name.replace(b'Su', b'Ru')
print(f"student name: {student_name}, type: {type(student_name)}")