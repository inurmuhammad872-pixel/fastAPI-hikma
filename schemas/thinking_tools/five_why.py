from pydantic import BaseModel
from typing import List


class FiveWhyRequest(BaseModel):
    problem: str


class FiveWhyResponse(BaseModel):
    problem: str
    why_1: str
    why_2: str
    why_3: str
    why_4: str
    root_cause: str
    conclusion: str