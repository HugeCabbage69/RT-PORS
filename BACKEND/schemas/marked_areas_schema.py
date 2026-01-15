from pydantic import BaseModel
from typing import List

class areas_get(BaseModel):
    coordinate:List[List[float]]
class areas_put(BaseModel):
    coordinate:List[float]
    type:str