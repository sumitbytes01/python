from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # this field is required
        min_length=5,
        max_length=15,
        description="Employee name",
        examples="Sumit Pareek"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000
    )


class User(BaseModel):
    email: str = Field(
        ...,
        regex=r''
    )
    phone: str = Field(
        ...,
        regex=r''
    )
    age: int = Field(
        ...,
        ge=0,
        le=100,
        description="age in years"
    )
    discount: float = Field(
        ...,
        ge=0
        le=100,
        description="Dicsount percentage"
    )
