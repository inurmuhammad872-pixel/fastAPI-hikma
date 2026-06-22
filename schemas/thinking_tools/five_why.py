from pydantic import BaseModel


class FiveWhyQuestionRequest(BaseModel):

    problem: str


class FiveWhyAnalyzeRequest(BaseModel):

    problem: str

    answers: list[str]