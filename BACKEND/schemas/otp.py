from pydantic import BaseModel


class LoginRequest(BaseModel):
    first_name: str
    last_name: str
    phone: str

class OTPVerify(BaseModel):
    phone: str
    otp: str