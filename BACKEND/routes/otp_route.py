from fastapi import APIRouter,Header
from schemas.otp import LoginRequest, OTPVerify
import random
import time
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
@router.get("/me")
def get_profile(token: str = Header(None)):
    if not token:
        return {"error": "Unauthorized"}

    phone = token.replace("TOKEN-", "")
    users = read_json(USERS_FILE)

    user = users.get(phone)
    if not user:
        return {"error": "User not found"}

    return user


@router.post("/send-otp")
def send_otp(data: LoginRequest):
    users = read_json(USERS_FILE)
    otps = read_json(OTPS_FILE)

    otp = str(random.randint(100000, 999999))

    otps[data.phone] = {
        "otp": otp,
        "expires": time.time() + 300
    }

    users[data.phone] = {
        "first_name": data.first_name,
        "last_name": data.last_name,
        "phone": data.phone
    }

    write_json(USERS_FILE, users)
    write_json(OTPS_FILE, otps)

    print(f"OTP for {data.phone} is {otp}")

    return {"message": "OTP sent"}


@router.post("/verify-otp")
def verify_otp(data: OTPVerify):
    users = read_json(USERS_FILE)
    otps = read_json(OTPS_FILE)

    record = otps.get(data.phone)
    if not record:
        return {"success": False, "message": "OTP not found"}

    if time.time() > record["expires"]:
        return {"success": False, "message": "OTP expired"}

    if data.otp != record["otp"]:
        return {"success": False, "message": "Invalid OTP"}

    # Optionally delete OTP after success
    del otps[data.phone]
    write_json(OTPS_FILE, otps)

    return {
        "success": True,
        "user": users[data.phone],
        "token": f"TOKEN-{data.phone}"
    }
@router.get("/test")
def test():
    a = read_json(USERS_FILE)
    return {"message":"working"}