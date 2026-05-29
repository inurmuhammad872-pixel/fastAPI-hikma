from pydantic import BaseModel
from typing import List


class DecisionMatrixRequest(BaseModel):
    decision: str
    options: List[str]
    criteria: List[str]