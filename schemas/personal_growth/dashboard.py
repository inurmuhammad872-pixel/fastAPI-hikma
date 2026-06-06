from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_goals: int
    completed_goals: int
    total_skills: int
    total_habits: int