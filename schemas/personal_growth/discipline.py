from pydantic import BaseModel


class HabitCreate(BaseModel):
    user_id: str
    name: str


class HabitToggle(BaseModel):
    completed: bool