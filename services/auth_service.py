# services/auth_service.py

from sqlalchemy.orm import Session
from db.models.user import User
from core.security import verify_password
from core.auth import create_access_token
from fastapi import HTTPException


def login_user(db: Session, data):

    user = None

    if data.email:
        user = db.query(User).filter(User.email == data.email).first()

    elif data.phone:
        user = db.query(User).filter(User.phone == data.phone).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, str(user.hashed_password)):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_access_token({
        "sub": str(user.id),
        "email": user.email,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }