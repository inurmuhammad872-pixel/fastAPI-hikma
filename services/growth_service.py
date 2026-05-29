from sqlalchemy.orm import Session

from db.models.growth_question import GrowthQuestion
from db.models.growth_answer import GrowthAnswer


def get_questions_by_category(db: Session, category: str):
    return db.query(GrowthQuestion).filter(
        GrowthQuestion.category == category
    ).all()


def create_answer(
    db: Session,
    user_id: int,
    question_id: int,
    answer: str
):
    new_answer = GrowthAnswer(
        user_id=user_id,
        question_id=question_id,
        answer=answer
    )

    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)

    return new_answer


def get_user_answers(db: Session, user_id: int):
    return db.query(GrowthAnswer).filter(
        GrowthAnswer.user_id == user_id
    ).all()