from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self)-> float:
        return self.price * self.quantity 
    
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(
        ...,
        ge=1
    )
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.rate_per_night * self.nights
    
booking = Booking(user_id=1, room_id=2, nights=2, rate_per_night=2000)

print(booking.total_amount)
print(booking.model_dump)