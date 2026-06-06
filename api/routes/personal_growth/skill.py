from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal

from schemas.personal_growth.skill import (
    SkillCreate,
    SkillUpdate
)

from services.personal_growth.skill_service import (
    create_skill,
    get_skills,
    update_skill,
    delete_skill
)

router = APIRouter(
    prefix="/personal-growth/skills",
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
    data: SkillCreate,
    db: Session = Depends(get_db)
):
    return create_skill(db, data)


@router.get("/{user_id}")
def list_skills(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_skills(db, user_id)


@router.put("/{skill_id}")
def update(
    skill_id: str,
    data: SkillUpdate,
    db: Session = Depends(get_db)
):
    return update_skill(
        db,
        skill_id,
        data.score
    )


@router.delete("/{skill_id}")
def delete(
    skill_id: str,
    db: Session = Depends(get_db)
):
    return delete_skill(
        db,
        skill_id
    )