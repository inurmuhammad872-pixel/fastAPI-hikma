from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal
from schemas.user import TypeACreate, TypeBCreate, TypeCCreate
from services.user_service import (
    create_type_a_user,
    create_type_b_user,
    create_type_c_user
)

router = APIRouter(prefix="/register", tags=["Register"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/type_a")
def register_type_a(user: TypeACreate, db: Session = Depends(get_db)):
    return create_type_a_user(db, user)


@router.post("/type_b")
def register_type_b(user: TypeBCreate, db: Session = Depends(get_db)):
    return create_type_b_user(db, user)


@router.post("/type_c")
def register_type_c(user: TypeCCreate, db: Session = Depends(get_db)):
    return create_type_c_user(db, user)