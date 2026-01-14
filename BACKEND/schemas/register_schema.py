from pydantic import BaseModel,Field


class RegisterUser(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    phone_number: str = Field(..., min_length=10, max_length=12)
