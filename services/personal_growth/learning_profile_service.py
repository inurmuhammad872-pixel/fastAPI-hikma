from db.models.personal_growth.goal import Goal
from db.models.personal_growth.skill import Skill
from db.models.personal_growth.discipline import Habit
from db.models.personal_growth.self_assessment import SelfAssessment

from services.ai.learning_profile_service import (
    generate_learning_profile
)


def get_learning_profile(
    db,
    user_id
):

    goals = db.query(
        Goal
    ).filter(
        Goal.user_id == user_id
    ).all()

    skills = db.query(
        Skill
    ).filter(
        Skill.user_id == user_id
    ).all()

    habits = db.query(
        Habit
    ).filter(
        Habit.user_id == user_id
    ).all()

    assessment = db.query(
        SelfAssessment
    ).filter(
        SelfAssessment.user_id == user_id
    ).order_by(
        SelfAssessment.created_at.desc()
    ).first()

    data = {

        "goals": [
            goal.title
            for goal in goals
        ],

        "skills": [

            {
                "name": skill.name,

                "score": skill.score

            }

            for skill in skills
        ],

        "habits": [
            habit.name
            for habit in habits
        ],

        "assessment": (

            {
                "confidence": assessment.confidence,

                "motivation": assessment.motivation,

                "focus": assessment.focus,

                "social": assessment.social,

                "stress": assessment.stress

            }

            if assessment

            else {}
        )
    }

    ai_result = generate_learning_profile(
        data
    )

    return {

        "student_data": data,

        "learning_profile": ai_result
    }