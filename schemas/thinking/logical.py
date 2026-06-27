from pydantic import BaseModel


class LogicalQuestionRequest(BaseModel):
    scenario: str


class LogicalAnswerRequest(BaseModel):
    question_id: int
    step: int
    ai_question: str
    answer: str


class LogicalAnalyzeRequest(BaseModel):
    question_id: int