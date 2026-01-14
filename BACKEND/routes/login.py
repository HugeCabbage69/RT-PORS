from fastapi import APIRouter,HTTPException
from schemas.login_schema import login
import requests
import json
import os

router = APIRouter(prefix="/login",tags=["LOGIN"])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")


# ---------- Helpers ----------
def read_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

@router.post("/user")
def do_login(data:login):
    user_db = read_json(USERS_FILE)
    for i in user_db:
        if i == data.phone:
            payload = {"phone":str(data.phone)}
            # MAKE CODE TO GET USER INPUT FOR OTP AND VERIFY IT
            otp = requests.post("/otp/send-otp",json=payload)
    raise HTTPException(status_code=400, detail="Phone number NOT registered")