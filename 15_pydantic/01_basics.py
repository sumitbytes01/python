from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data= {
    'id': 123, 'name': 'Sumit', "is_active": True
}
input_data1= {
    'id': 123, 'name': 'Sumit', "is_active": 24
}

input_data2= {
    'id': '345', 'name': 'Sumit', "is_active": True
}

user = User(**input_data)
print(user)

# user2 = User(**input_data2)
# print(user2)

# user1 = User(**input_data1)
# print(user1)

