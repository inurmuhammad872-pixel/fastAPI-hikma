from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas.personal_growth.self_awareness import (
    SelfAwarenessAnswerCreate
)

from services.personal_growth.self_awareness_service import (
    create_answer
)


router = APIRouter(
    prefix="/personal-growth/self-awareness",
    tags=["Personal Growth"]
)

@router.get("/questions")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def questions(
    db: Session = Depends(get_db)
):
    return get_questions(db)
@router.post("/answer")
def save_answer(
    data: SelfAwarenessAnswerCreate,
    db: Session = Depends(get_db)
):
    return create_answer(
        db,
        data
    )