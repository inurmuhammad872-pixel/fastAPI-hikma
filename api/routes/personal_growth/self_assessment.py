from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas.personal_growth.self_assessment import (
    SelfAssessmentCreate
)

from services.personal_growth.self_assessment_service import (
    create_assessment,
    get_history,
    get_latest
)

router = APIRouter(
    prefix="/personal-growth/self-assessment",
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
    data: SelfAssessmentCreate,
    db: Session = Depends(get_db)
):
    return create_assessment(
        db,
        data
    )


@router.get("/history/{user_id}")
def history(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_history(
        db,
        user_id
    )


@router.get("/latest/{user_id}")
def latest(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_latest(
        db,
        user_id
    )