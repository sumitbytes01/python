from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def name_must_be_capitalised(cls, value):
        if not value.istitle():
            raise ValueError("Names must be capitalised")
        return value
    
class User(BaseModel):
    email: str

    @field_validator("email")
    def normalise_email(cls, v):
        return v.lower().strip()
    
class Product(BaseModel):
    price: str

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', '').replace(',',''))
        return v

class DateRange(BaseModel):
    starte_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls, v):
        if v.start_date >= v.end_date:
            raise ValueError("End date must be greater than start date")
        return v