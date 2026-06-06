from pydantic import BaseModel


class GoalCreate(BaseModel):
    user_id: str
    title: str


class GoalUpdate(BaseModel):
    completed: bool


class GoalResponse(BaseModel):
    id: str
    user_id: str
    title: str
    completed: bool

    class Config:
        from_attributes = True


class GoalCreateResponse(BaseModel):
    id: str
    message: str