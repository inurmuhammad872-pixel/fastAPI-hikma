from pydantic import BaseModel


class PDSARequest(BaseModel):
    goal: str
    current_problem: str