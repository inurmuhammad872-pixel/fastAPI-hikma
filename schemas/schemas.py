from datetime import date
from pydantic import BaseModel
from typing import Optional

# TYPE USERS
class TypeACreate(BaseModel):
    first_name: str
    last_name: str
    father_name: str
    phone: str
    gender: str
    birth_date: date
    region: str
    district: str
    role: str = "type_a"
    password: str   # 🔥 qo‘shildi


class TypeBCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    relation: str
    reference_code: Optional[str] = None
    role: str = "type_b"
    password: str   # 🔥


class TypeCCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    gender: str
    teacher_type: str
    subject: str
    role: str = "type_c"
    password: str   # 🔥


# AUTH
class UserLogin(BaseModel):
    phone: str
    password: str