from fastapi import APIRouter,Header
from schemas.otp_schema import OTP
import random
import json
import os

router = APIRouter(prefix="/get-marked-areas",tags=["MARKED-AREAS"])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.json")
OTPS_FILE = os.path.join(DATA_DIR, "otps.json")
