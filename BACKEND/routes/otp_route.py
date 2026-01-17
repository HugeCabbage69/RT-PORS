from fastapi import APIRouter, Header
from schemas.otp_schema import OTP
import random
import json
import os
from datetime import datetime, timedelta

router = APIRouter(prefix="/otp", tags=["OTP"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")
OTPS_FILE = os.path.join(DATA_DIR, "otps.json")


def read_json(path: str) -> dict:
    """Read JSON file and return as dict."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict):
    """Write dict to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@router.post("/send-otp")
def send_otp(data: OTP):
    """Send OTP to user's phone and store in JSON."""
    otps = read_json(OTPS_FILE)
    

    otp = str(random.randint(100000, 999999))
    
    # Store OTP with expiry (10 minutes)
    otp_data = {
        "otp": otp,
        "created_at": datetime.now().isoformat(),
        "expires_at": (datetime.now() + timedelta(minutes=10)).isoformat(),
        "attempts": 0
    }
    
    otps[data.phone] = otp_data
    write_json(OTPS_FILE, otps)
    

    print(f"OTP for {data.phone} is {otp}")
    
    return {"message": "OTP sent successfully", "otp": otp}  # For testing only


