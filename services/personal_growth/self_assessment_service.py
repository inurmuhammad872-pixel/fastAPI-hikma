from db.models.personal_growth.self_assessment import (
    SelfAssessment
)


def create_assessment(
    db,
    data
):

    assessment = SelfAssessment(
        user_id=data.user_id,
        confidence=data.confidence,
        motivation=data.motivation,
        focus=data.focus,
        social=data.social,
        stress=data.stress
    )

    db.add(assessment)

    db.commit()

    db.refresh(assessment)

    return {
        "id": assessment.id,
        "message": "Assessment created"
    }


def get_history(
    db,
    user_id
):

    return db.query(
        SelfAssessment
    ).filter(
        SelfAssessment.user_id == user_id
    ).all()


def get_latest(
    db,
    user_id
):

    return db.query(
        SelfAssessment
    ).filter(
        SelfAssessment.user_id == user_id
    ).order_by(
        SelfAssessment.created_at.desc()
    ).first()