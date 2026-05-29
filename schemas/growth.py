from pydantic import BaseModel
from enum import Enum


class GrowthCategory(str, Enum):
    SELF_AWARENESS = "self_awareness"
    SKILLS = "skills"
    DISCIPLINE = "discipline"


class QuestionResponse(BaseModel):
    id: int
    question: str

    class Config:
        from_attributes = True


class AnswerCreate(BaseModel):
    question_id: int
    answer: str


class AnswerResponse(BaseModel):
    id: int
    question_id: int
    answer: str

    class Config:
        from_attributes = True