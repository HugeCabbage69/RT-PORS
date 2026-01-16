from fastapi import APIRouter, HTTPException
from schemas.login_schema import login, verify_otp_schema
from utils.auth_utils import create_session, verify_token, read_json, USERS_FILE
import requests
import json
import os

router = APIRouter(prefix="/login", tags=["LOGIN"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OTPS_FILE = os.path.join(DATA_DIR, "otps.json")


def write_json(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@router.post("/user")
def do_login(data: login):
    """Initiate login by sending OTP to verified user."""
    user_db = read_json(USERS_FILE)
    
    # Check if phone number is registered
    if data.phone not in user_db:
        raise HTTPException(status_code=400, detail="Phone number NOT registered")
    
    payload = {"phone": str(data.phone)}
    # Send OTP to the phone number
    try:
        otp_response = requests.post("http://localhost:8000/otp/send-otp", json=payload)
        return {"message": "OTP sent successfully", "phone": data.phone}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send OTP")


@router.post("/verify-otp")
def verify_otp_and_login(data: verify_otp_schema):
    """Verify OTP and create session token for multiple concurrent logins."""
    otps_db = read_json(OTPS_FILE)
    user_db = read_json(USERS_FILE)
    
    # Check if user exists
    if data.phone not in user_db:
        raise HTTPException(status_code=400, detail="Phone number NOT registered")
    
    # Check if OTP exists and matches
    if data.phone not in otps_db or otps_db[data.phone].get("otp") != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    
    # OTP is valid, remove it from database
    del otps_db[data.phone]
    write_json(OTPS_FILE, otps_db)
    
    # Create a new session (multiple sessions can exist for same user)
    session = create_session(data.phone)
    
    user_info = user_db[data.phone]
    return {
        "message": "Login successful",
        "token": session["token"],
        "phone": session["phone"],
        "first_name": user_info.get("first_name"),
        "last_name": user_info.get("last_name"),
        "expires_at": session["expires_at"]
    }


@router.post("/logout")
def do_logout(token: str):
    """Logout user by deactivating their session token."""
    from utils.auth_utils import logout
    
    if logout(token):
        return {"message": "Logged out successfully"}
    
    raise HTTPException(status_code=400, detail="Invalid token")