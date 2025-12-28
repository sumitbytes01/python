from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) <4:
            raise ValueError("Username must be atleast 4 chars long")
        return v
    
class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, v):
        if v.password != v.confirm_password:
            raise ValueError("Passwords do not match")
        return v
