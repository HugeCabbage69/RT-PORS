from pydantic import BaseModel


class OTP(BaseModel):
    phone: str
