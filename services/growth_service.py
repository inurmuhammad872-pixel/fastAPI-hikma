from sqlalchemy.orm import Session

from db.models.thinking_tools.growth_question import GrowthQuestion
from db.models.thinking_tools.growth_answer import GrowthAnswer

from services.ai.logical_service import (
    generate_logical_questions,
    analyze_logical_answers
)


# ===========================
# Growth (Old)
# ===========================

def get_questions_by_category(
    db: Session,
    category: str
):
    return db.query(
        GrowthQuestion
    ).filter(
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


def get_user_answers(
    db: Session,
    user_id: int
):

    return db.query(
        GrowthAnswer
    ).filter(
        GrowthAnswer.user_id == user_id
    ).all()


# ===========================
# Logical Thinking AI
# ===========================

def generate_ai_questions(
    scenario: str
):

    return generate_logical_questions(
        scenario
    )


def save_logical_answer(
    db: Session,
    user_id: int,
    question_id: int,
    step: int,
    ai_question: str,
    answer: str
):

    new_answer = GrowthAnswer(

        user_id=user_id,

        question_id=question_id,

        step=step,

        ai_question=ai_question,

        answer=answer

    )

    db.add(new_answer)

    db.commit()

    db.refresh(new_answer)

    return new_answer


def analyze_answers(
    db: Session,
    question_id: int
):

    answers = db.query(
        GrowthAnswer
    ).filter(
        GrowthAnswer.question_id == question_id
    ).order_by(
        GrowthAnswer.step
    ).all()

    answer_list = [

        item.answer

        for item in answers

    ]

    result = analyze_logical_answers(

        "",

        answer_list

    )

    for item in answers:

        item.ai_feedback = result

    db.commit()

    return result