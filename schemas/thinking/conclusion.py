from pydantic import BaseModel


class ConclusionRequest(BaseModel):
    question: str
    answer: str