from fastapi import APIRouter,Header
from schemas.otp_schema import OTP
import random
import json
import os

router = APIRouter(prefix="/otp",tags=["OTP"])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")
OTPS_FILE = os.path.join(DATA_DIR, "otps.json")

# ---------- Helpers ----------
def read_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ---------- Routes ----------

# STILL HAVE TO MAKE A WORKING CODE TO SEND OTP
@router.post("/send-otp")
def send_otp(data: OTP):
    otps = read_json(OTPS_FILE)

    otp = str(random.randint(100000, 999999))

    write_json(OTPS_FILE, otps)

    print(f"OTP for {data.phone} is {otp}")

    return {"message": otp}

