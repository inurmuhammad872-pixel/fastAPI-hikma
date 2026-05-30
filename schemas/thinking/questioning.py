from pydantic import BaseModel


class QuestioningRequest(BaseModel):
    question: str
    answer: str