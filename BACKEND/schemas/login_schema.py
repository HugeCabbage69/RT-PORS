from pydantic import BaseModel


class login(BaseModel):
    phone: str