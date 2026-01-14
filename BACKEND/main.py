from fastapi import FastAPI
from routes import otp_route,register,login

app = FastAPI()

app.include_router(otp_route.router)
app.include_router(register.router)
app.include_router(login.router)