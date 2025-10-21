# Strings
hobby = "coding"
student_name = "Sumit"
print(f"student name: {student_name}, hobby is: {hobby}")

nice_string = "this is a very nice string"
print(f"nice string: {nice_string}, type: {type(nice_string)}")
print(f"length of nice string: {len(nice_string)}")

print(f"first character: {nice_string[0]}")

print(f"last character: {nice_string[-1]}")

print(f"substring: {nice_string[1:3]}")

print(f"substring with skip: {nice_string[1:20:2]}")

multiline_string = """this is a multiline string
i can write anything here
like this
1234567890
!@#$%^&*()_+
"""
print(f"multiline string: {multiline_string}, type: {type(multiline_string)}")

escaped_string = "this is a \"escaped\" string"
print(f"escaped string: {escaped_string}, type: {type(escaped_string)}")

raw_string = r"this is a \n raw string"
print(f"raw string: {raw_string}, type: {type(raw_string)}")

formatted_string = f"student name is {student_name}, hobby is {hobby}"
print(f"formatted string: {formatted_string}, type: {type(formatted_string)}")
upper_string = nice_string.upper()
print(f"upper string: {upper_string}, type: {type(upper_string)}")

lower_string = nice_string.lower()
print(f"lower string: {lower_string}, type: {type(lower_string)}")

split_string = nice_string.split(" ") # list
print(f"split string: {split_string}, type: {type(split_string)}")

joined_string = " ".join(split_string)
print(f"joined string: {joined_string}, type: {type(joined_string)}")

replaced_string = nice_string.replace("nice", "awesome")
print(f"replaced string: {replaced_string}, type: {type(replaced_string)}")

trimmed_string = "   this is a trimmed string   ".strip()
print(f"trimmed string: '{trimmed_string}', type: {type(trimmed_string)}")

index_of_string = nice_string.index("very")
print(f"index of string: {index_of_string}, type: {type(index_of_string)}")

find_index_of_string = nice_string.find("very")
print(f"find index of string: {find_index_of_string}, type: {type(find_index_of_string)}")

not_found_index = nice_string.find("bad")
print(f"not found index: {not_found_index}, type: {type(not_found_index)}")

count_of_string = nice_string.count("is")
print(f"count of string: {count_of_string}, type: {type(count_of_string)}")
print(nice_string)

print(nice_string[:3])
print(nice_string[1:])
print(nice_string[::-1])

label_text = "this is label tひxt"
print(f"this is label text: {label_text}")
encoded_text = label_text.encode("utf-8")
print(f"this is encoded text:{encoded_text}")
print(f"this is decoded text:{encoded_text.decode('utf-8')}")

