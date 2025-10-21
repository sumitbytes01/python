# boolean data type

is__mohit_passed = True
print(f"is passed: {is__mohit_passed}, type: {type(is__mohit_passed)}")

student_passed = 50

total_of_student_passed = student_passed + is__mohit_passed # upcasting
print(f"total of student passed: {total_of_student_passed}, type: {type(total_of_student_passed)}")

sumit_passed = 0
print(f"sumit passed: {sumit_passed}, type: {bool(sumit_passed)}")

anu_passed = 1
print(f"anu passed: {anu_passed}, type: {bool(anu_passed)}")

thiya_passed = 100
print(f"thiya passed: {thiya_passed}, type: {bool(thiya_passed)}")

padosi_passed = None
print(f"padosi passed: {padosi_passed}, type: {bool(padosi_passed)}")

# logical operations
sumit_passed = False
both_passed = is__mohit_passed and sumit_passed
print(f"both passed: {both_passed}, type: {type(both_passed)}")

any_passed = is__mohit_passed or sumit_passed
print(f"any passed: {any_passed}, type: {type(any_passed)}")