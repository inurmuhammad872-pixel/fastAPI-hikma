from pydantic import BaseModel


class SelfAwarenessAnswerCreate(BaseModel):
    user_id: str
    question_id: str
    answer: str


class SelfAwarenessResponse(BaseModel):
    id: str
    message: str

class SelfAwarenessQuestionResponse(BaseModel):
    id: str
    question: str

    class Config:
        from_attributes = True