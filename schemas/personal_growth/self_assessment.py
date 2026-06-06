from pydantic import BaseModel


class SelfAssessmentCreate(BaseModel):
    user_id: str
    confidence: int
    motivation: int
    focus: int
    social: int
    stress: int


class SelfAssessmentResponse(BaseModel):
    id: str
    user_id: str

    confidence: int
    motivation: int
    focus: int
    social: int
    stress: int

    class Config:
        from_attributes = True