from pydantic import BaseModel


class DISCRequest(BaseModel):
    dominance: int
    influence: int
    steadiness: int
    conscientiousness: int