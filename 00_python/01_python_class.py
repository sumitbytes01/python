class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
       
    def display_info(self):
        print(f"""Name: {self.name}
            Age: {self.age}
            Roll Number: {self.roll_number}""")
    
    @classmethod
    def create_new_student(cls, name, age, roll_number):
        return cls(name, age, roll_number)
    
# Example usage
student1 = Student("Alice", 20, 101)
student1.display_info()
student2 = Student.create_new_student("Bob", 22, 102)
student2.display_info()
student1 = Student(name="Sumit", age=37, roll_number=142)

