from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal
from schemas.auth import UserLogin, GoogleTokenRequest
from services.auth_service import login_user

from db.models.user import User
from core.auth import create_access_token

import httpx

router = APIRouter(
    prefix="",
    tags=["Auth"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# NORMAL LOGIN
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(db, user)


# GOOGLE LOGIN
@router.post("/auth/google")
async def google_login(
    body: GoogleTokenRequest,
    db: Session = Depends(get_db)
):

    print("GOOGLE LOGIN HIT")

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={
                "Authorization":
                f"Bearer {body.access_token}"
            }
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=401,
            detail="Invalid Google token"
        )

    google_user = response.json()

    print(google_user)

    email = google_user.get("email")

    if not email:
        raise HTTPException(
            status_code=400,
            detail="Google email not found"
        )

    # FIND USER
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # CREATE JWT
    token = create_access_token({
        "sub": str(user.id),
        "email": user.email,
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }