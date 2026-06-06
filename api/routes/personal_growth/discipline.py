from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas.personal_growth.discipline import (
    HabitCreate,
    HabitToggle
)

from services.personal_growth.discipline_service import (
    create_habit,
    get_habits,
    toggle_habit
)


router = APIRouter(
    prefix="/personal-growth/discipline",
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
    data: HabitCreate,
    db: Session = Depends(get_db)
):
    return create_habit(
        db,
        data
    )


@router.get("/{user_id}")
def habits(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_habits(
        db,
        user_id
    )


@router.post("/{habit_id}/toggle")
def toggle(
    habit_id: str,
    data: HabitToggle,
    db: Session = Depends(get_db)
):
    return toggle_habit(
        db,
        habit_id,
        data.completed
    )