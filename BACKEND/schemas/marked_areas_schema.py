from pydantic import BaseModel
from typing import List

class areas(BaseModel):
    coordinate:List[List[int]]