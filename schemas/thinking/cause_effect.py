from pydantic import BaseModel


class CauseEffectRequest(BaseModel):
    question: str
    answer: str