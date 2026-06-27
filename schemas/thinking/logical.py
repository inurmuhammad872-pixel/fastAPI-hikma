from pydantic import BaseModel


class LogicalQuestionRequest(BaseModel):
    scenario: str


class LogicalQuestionResponse(BaseModel):
    questions: list[str]


class LogicalAnswerItem(BaseModel):
    question: str
    answer: str


class LogicalAnalyzeRequest(BaseModel):
    scenario: str
    answers: list[LogicalAnswerItem]