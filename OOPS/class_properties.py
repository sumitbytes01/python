class PropertyPlay:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age+2
    
    @age.setter
    def age(self, age):
        if 1<= age <=5:
            self._age = age
        else:
            raise ValueError("Age shoud be between a and 5 years")

pp = PropertyPlay(2)
print(pp.age)

pp.age = 5
print(pp.age)