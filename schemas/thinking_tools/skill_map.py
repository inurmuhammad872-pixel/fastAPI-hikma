from pydantic import BaseModel


class SkillMapRequest(BaseModel):
    communication: int
    leadership: int
    creativity: int
    discipline: int
    teamwork: int