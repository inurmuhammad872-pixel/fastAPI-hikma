from datetime import date
from pydantic import BaseModel
from typing import Optional


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


class TypeBCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    relation: str
    password: str


class TypeCCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    password: str


class UserLogin(BaseModel):
    phone: str
    password: str