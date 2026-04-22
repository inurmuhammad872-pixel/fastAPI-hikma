from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TypeACreate(BaseModel):
    first_name: str
    last_name: str
    father_name: str
    phone: str
    gender: str
    birth_date: date
    region: str
    district: str
    password: str


class UserLogin(BaseModel):
    phone: str
    password: str
