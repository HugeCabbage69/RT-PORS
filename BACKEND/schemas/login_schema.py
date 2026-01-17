from pydantic import BaseModel


class login(BaseModel):
    phone: str


class verify_otp_schema(BaseModel):
    phone: str
    otp: str