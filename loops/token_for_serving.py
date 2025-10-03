for token in range(1,11):
    print(f"serving chai to token number: {token}")

for batch in range(1,5):
    print(f"serving chai for batch number: {batch}")

student_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"]
for name in student_names:
    print(f"serving chai to student: {name}")

seasons = ["Spring", "Summer", "Autumn", "Winter"]
for idx,season in enumerate(seasons):
    print(f"Season {idx}: {season}")

seasons = ["Spring", "Summer", "Autumn", "Winter"]
for idx,season in enumerate(seasons, start=1):
    print(f"Season {idx}: {season}")

for idx, _ in enumerate(seasons):
    print(f"Index: {idx}")

enum_list = list(enumerate(seasons))
print(enum_list)  # [(0, 'Spring'), (1, 'Summer'), (2, 'Autumn'), (3, 'Winter')]

for idx, char in enumerate("hello"):
    print(idx, char)

student_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"]
student_marks = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]

for name, mark in zip(student_names, student_marks):
    print(f"{name} scored {mark} marks")