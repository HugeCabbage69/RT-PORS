from fastapi import APIRouter,HTTPException
from schemas.register import RegisterUser

import json
import os

router = APIRouter(prefix="/register",tags=["REGISTER"])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")

# ---------- Helpers ----------
def get_user_data(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_user_data(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@router.post("/user")

def register_user(user: RegisterUser):

    users_db = get_user_data(USERS_FILE)
    # Check if phone number already exists
    for u in users_db:
        if u == user.phone_number:
            raise HTTPException(status_code=400, detail="Phone number already registered")

    new_user = {
        "first_name": user.first_name,
        "last_name": user.last_name,
    }

    users_db[user.phone_number] = new_user
    write_user_data(USERS_FILE,users_db)
    return {"message":"registration succesfull"}
