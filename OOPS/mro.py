class A:
    label = "A: Base Class"

class B(A):
    label = "B: Cold Blend"

class C(A):
    label = "C: Herbal Coffee"

class D(B,C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)