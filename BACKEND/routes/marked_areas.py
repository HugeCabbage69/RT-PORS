from fastapi import APIRouter,Header
from schemas.marked_areas_schema import areas_put,areas_get
import os
import json
router = APIRouter(prefix="/marked-areas",tags=["MARKED-AREAS"])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

AREAS_FILE = os.path.join(DATA_DIR, "marked_areas.json")


def read_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@router.get("/recieve")
def get():
    areas_data = read_json(AREAS_FILE)
    return areas_data
@router.post("/put")
def put(data:areas_put):
    areas_data = read_json(AREAS_FILE)
    print(areas_data)
    print(type(data.coordinate))
    areas_data["areas"].append(data.coordinate)
    print(areas_data)
    write_json(AREAS_FILE,areas_data)
    return {"message":"succesfull"}