# services/auth_service.py

from sqlalchemy.orm import Session
from db.models.user import (
    User,
    TypeAUser,
    TypeBUser,
    TypeCUser
)

from core.security import verify_password
from core.auth import create_access_token
from fastapi import HTTPException


def login_user(db: Session, data):

    user = None

    # LOGIN WITH EMAIL
    if data.email:
        user = db.query(User).filter(
            User.email == data.email
        ).first()

    # LOGIN WITH PHONE
    elif data.phone:

        profile = (
            db.query(TypeAUser).filter(
                TypeAUser.phone == data.phone
            ).first()

            or

            db.query(TypeBUser).filter(
                TypeBUser.phone == data.phone
            ).first()

            or

            db.query(TypeCUser).filter(
                TypeCUser.phone == data.phone
            ).first()
        )

        if profile:
            user = db.query(User).filter(
                User.id == profile.id
            ).first()

    # USER NOT FOUND
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # PASSWORD CHECK
    if not verify_password(
        data.password,
        str(user.hashed_password)
    ):
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )

    # CREATE TOKEN
    token = create_access_token({
        "sub": str(user.id),
        "email": user.email,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

