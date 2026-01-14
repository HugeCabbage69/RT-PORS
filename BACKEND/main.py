from fastapi import FastAPI
from routes import otp_route

app = FastAPI()

app.include_router(otp_route.router)