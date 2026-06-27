from pydantic import BaseModel


from pydantic import BaseModel


class LogicalQuestionRequest(BaseModel):
    scenario: str


class LogicalQuestionResponse(BaseModel):
    questions: list[str]


class LogicalAnswerItem(BaseModel):
    question: str
    answer: str


class LogicalAnswerRequest(BaseModel):
    question_id: int
    step: int
    ai_question: str
    answer: str


class LogicalAnalyzeRequest(BaseModel):
    question_id: int