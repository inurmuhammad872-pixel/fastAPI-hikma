from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from db.database import SessionLocal

from services.personal_growth.learning_profile_service import (
    get_learning_profile
)

router = APIRouter(
    prefix="/personal-growth/learning-profile",
    tags=["Learning Profile"]
)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.get("/{user_id}")
def learning_profile(
    user_id: str,
    db: Session = Depends(get_db)
):

    return get_learning_profile(
        db,
        user_id
    )