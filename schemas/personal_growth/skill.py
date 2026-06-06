from pydantic import BaseModel


class SkillCreate(BaseModel):
    user_id: str
    name: str
    score: int


class SkillUpdate(BaseModel):
    score: int


class SkillResponse(BaseModel):
    id: str
    name: str
    score: int

    class Config:
        from_attributes = True