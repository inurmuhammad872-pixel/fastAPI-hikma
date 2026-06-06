from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas.personal_growth.career import (
    CareerInterestCreate
)

from services.personal_growth.career_service import (
    create_interest,
    get_interests,
    delete_interest
)

router = APIRouter(
    prefix="/personal-growth/career",
    tags=["Personal Growth"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create(
    data: CareerInterestCreate,
    db: Session = Depends(get_db)
):
    return create_interest(
        db,
        data
    )


@router.get("/{user_id}")
def interests(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_interests(
        db,
        user_id
    )


@router.delete("/{interest_id}")
def delete(
    interest_id: str,
    db: Session = Depends(get_db)
):
    return delete_interest(
        db,
        interest_id
    )