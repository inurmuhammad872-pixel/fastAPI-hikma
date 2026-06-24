from pydantic import BaseModel


class ObserveQuestionRequest(BaseModel):

    scenario: str


class ObserveAnalyzeRequest(BaseModel):

    scenario: str

    answers: list[str]


class ObserveConclusionRequest(BaseModel):

    scenario: str

    observe: str

    reason: str

    evidence: str

    alternative: str

    conclusion: str