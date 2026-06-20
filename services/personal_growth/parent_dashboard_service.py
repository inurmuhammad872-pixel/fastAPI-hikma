from db.models.personal_growth.goal import Goal
from db.models.personal_growth.skill import Skill
from db.models.personal_growth.discipline import Habit
from db.models.personal_growth.self_assessment import SelfAssessment

from services.ai.parent_summary_service import generate_parent_summary


def get_parent_dashboard(
    db,
    user_id
):

    goals_count = db.query(
        Goal
    ).filter(
        Goal.user_id == user_id
    ).count()

    completed_goals = db.query(
        Goal
    ).filter(
        Goal.user_id == user_id,
        Goal.completed == True
    ).count()

    skills = db.query(
        Skill
    ).filter(
        Skill.user_id == user_id
    ).all()

    habits_count = db.query(
        Habit
    ).filter(
        Habit.user_id == user_id
    ).count()

    latest_assessment = db.query(
        SelfAssessment
    ).filter(
        SelfAssessment.user_id == user_id
    ).order_by(
        SelfAssessment.created_at.desc()
    ).first()

    dashboard_data = {

        "goals_count": goals_count,

        "completed_goals": completed_goals,

        "skills_count": len(skills),

        "habits_count": habits_count,

        "latest_assessment": (

            {
                "confidence": latest_assessment.confidence,

                "motivation": latest_assessment.motivation,

                "focus": latest_assessment.focus,

                "social": latest_assessment.social,

                "stress": latest_assessment.stress

            }

            if latest_assessment

            else "No assessment yet"
        )
    }

    ai_summary = generate_parent_summary(
        dashboard_data
    )

    return {

        "dashboard": dashboard_data,

        "ai_summary": ai_summary
    }