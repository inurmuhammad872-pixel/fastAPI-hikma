from pydantic import BaseModel, EmailStr
from typing import Optional


class UserRegister(BaseModel):
    phone: str
    password: str

class GoogleTokenRequest(BaseModel):
    access_token: str

class UserLogin(BaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    password: str