from pydantic import BaseModel


class CareerInterestCreate(BaseModel):
    user_id: str
    interest: str


class CareerInterestResponse(BaseModel):
    id: str
    user_id: str
    interest: str

    class Config:
        from_attributes = True