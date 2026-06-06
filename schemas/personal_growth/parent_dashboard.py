from pydantic import BaseModel


class ParentDashboardResponse(BaseModel):
    goals_count: int
    completed_goals: int
    skills_count: int
    habits_count: int