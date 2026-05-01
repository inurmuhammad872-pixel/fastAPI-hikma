from pydantic import BaseModel, EmailStr
from datetime import date

class TypeACreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    father_name: str
    phone: str
    gender: str
    birth_date: date
    region: str
    district: str
    
class TypeBCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    father_name: str
    phone: str
    gender: str
    birth_date: date
    region: str
    district: str
    relation: str

class TypeCCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    father_name: str
    phone: str
   
    
    