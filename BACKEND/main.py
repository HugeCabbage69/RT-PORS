from fastapi import FastAPI
from routes import otp_route,register

app = FastAPI()

app.include_router(otp_route.router)
app.include_router(register.router)