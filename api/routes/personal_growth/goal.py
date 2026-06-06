from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas.personal_growth.goal import (
    GoalCreate,
    GoalUpdate
)

from services.personal_growth.goal_service import (
    create_goal,
    get_goals,
    update_goal,
    delete_goal
)

router = APIRouter(
    prefix="/personal-growth/goals",
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
    data: GoalCreate,
    db: Session = Depends(get_db)
):
    return create_goal(
        db,
        data
    )


@router.get("/{user_id}")
def goals(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_goals(
        db,
        user_id
    )


@router.patch("/{goal_id}")
def update(
    goal_id: str,
    data: GoalUpdate,
    db: Session = Depends(get_db)
):
    return update_goal(
        db,
        goal_id,
        data.completed
    )


@router.delete("/{goal_id}")
def delete(
    goal_id: str,
    db: Session = Depends(get_db)
):
    return delete_goal(
        db,
        goal_id
    )