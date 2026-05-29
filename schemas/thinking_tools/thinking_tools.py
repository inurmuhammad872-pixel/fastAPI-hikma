from pydantic import BaseModel
from typing import List


class SWOTRequest(BaseModel):
    topic: str
    strengths: List[str]
    weaknesses: List[str]
    opportunities: List[str]
    threats: List[str]


class SWOTResponse(BaseModel):
    summary: str
    recommendation: str