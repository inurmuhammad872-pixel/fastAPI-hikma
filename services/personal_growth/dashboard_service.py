from db.models.personal_growth.goal import Goal
from db.models.personal_growth.skill import Skill
from db.models.personal_growth.self_assessment import SelfAssessment
from db.models.personal_growth.discipline import Habit


def get_dashboard(
    db,
    user_id
):

    total_goals = db.query(
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

    total_skills = db.query(
        Skill
    ).filter(
        Skill.user_id == user_id
    ).count()

    total_habits = db.query(
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

    return {
        "total_goals": total_goals,
        "completed_goals": completed_goals,
        "total_skills": total_skills,
        "total_habits": total_habits,
        "latest_assessment": latest_assessment
    }