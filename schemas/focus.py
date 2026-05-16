from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class FocusStartSchema(BaseModel):
    user_id: int
    duration: int = Field(
        gt=0,
        le=180
    )

class FocusSessionResponse(BaseModel):
    session_id: int
    user_id: int
    duration: int
    started_at: datetime
    ended_at: Optional[datetime]
    status: str