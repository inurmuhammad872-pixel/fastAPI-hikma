from sqlalchemy.orm import Session

from db.models.personal_growth.self_awareness import (
    SelfAwarenessAnswer
)

from services.ai.question_generator_service import (
    generate_questions
)

from db.models.personal_growth.self_awareness import (
    SelfAwarenessAnswer
)




def get_questions(db):

    return generate_questions(
        "self_awareness"
    )

def create_answer(
    db: Session,
    data
):

    answer = SelfAwarenessAnswer(
        user_id=data.user_id,
        question_id=data.question_id,
        answer=data.answer,
        ai_feedback=None
    )

    db.add(answer)

    db.commit()

    db.refresh(answer)

    return {
        "id": answer.id,
        "message": "Answer saved"
    }