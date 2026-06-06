from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal

from services.personal_growth.dashboard_service import (
    get_dashboard
)

router = APIRouter(
    prefix="/personal-growth/dashboard",
    tags=["Dashboard"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/{user_id}")
def dashboard(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_dashboard(
        db,
        user_id
    )