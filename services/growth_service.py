from sqlalchemy.orm import Session

from db.models.growth_answer import GrowthAnswer

from services.ai.question_generator_service import (
    generate_questions
)


def get_questions_by_category(
    db,
    category
):

    questions = generate_questions(
        category
    )

    result = []

    for index, question in enumerate(
        questions,
        start=1
    ):

        result.append(

            {
                "id": index,

                "question": question
            }

        )

    return result


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

    db.add(
        new_answer
    )

    db.commit()

    db.refresh(
        new_answer
    )

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