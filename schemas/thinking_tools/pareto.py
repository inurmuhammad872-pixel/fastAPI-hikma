from pydantic import BaseModel
from typing import List


class ParetoRequest(BaseModel):
    goal: str
    activities: List[str]