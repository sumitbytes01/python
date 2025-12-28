from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product1 = Product(id=1, name="mug", price=99, in_stock=True)
print(product1)

product2 = Product(id=2, name="mouse", price=9)
print(product2)

product2 = Product( name="mouse")
#print(product2)