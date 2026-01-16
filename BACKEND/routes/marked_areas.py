from fastapi import APIRouter, Header, HTTPException
from schemas.marked_areas_schema import areas_put, areas_get
from utils.auth_utils import verify_token, read_json, write_json
import os
import json

router = APIRouter(prefix="/marked-areas", tags=["MARKED-AREAS"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

AREAS_FILE = os.path.join(DATA_DIR, "marked_areas.json")


@router.get("/recieve")
def get(authorization: str = Header(None)):
    """Get marked areas for authenticated user."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token required")
    
    # Extract token from "Bearer <token>" format
    token = authorization.replace("Bearer ", "") if authorization.startswith("Bearer ") else authorization
    
    session = verify_token(token)
    if not session:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    phone = session["phone"]
    areas_data = read_json(AREAS_FILE)
    
    # Return only areas marked by this user
    user_areas = {}
    if phone in areas_data:
        user_areas = areas_data[phone]
    
    return {
        "phone": phone,
        "areas": user_areas
    }


@router.post("/put")
def put(data: areas_put, authorization: str = Header(None)):
    """Store marked area for authenticated user."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token required")
    
    # Extract token from "Bearer <token>" format
    token = authorization.replace("Bearer ", "") if authorization.startswith("Bearer ") else authorization
    
    session = verify_token(token)
    if not session:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    phone = session["phone"]
    areas_data = read_json(AREAS_FILE)
    
    # Store areas per user
    if phone not in areas_data:
        areas_data[phone] = {}
    
    if data.type in areas_data[phone]:
        areas_data[phone][data.type].append(data.coordinate)
    else:
        areas_data[phone][data.type] = [data.coordinate]
    
    write_json(AREAS_FILE, areas_data)
    
    return {
        "message": "Area saved successfully",
        "phone": phone,
        "type": data.type,
        "coordinate": data.coordinate
    }