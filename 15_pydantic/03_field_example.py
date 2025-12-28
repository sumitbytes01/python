from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    item: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

cart_data = {
    "user_id": 1, 
    "item": ["Laptop", "Keyboard", "Mouse"],
    "quantities": {"Laptop": 1, "Keyboard":2, "Mouse":1}
}
cart_data = Cart(**cart_data) # spread cart data
print(cart_data)
