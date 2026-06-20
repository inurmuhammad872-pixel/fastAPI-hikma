from services.ai.base_ai_service import ask_ai


def generate_parent_summary(data):

    system_prompt = """
You are an educational mentor inside Hikma platform.

Analyze student's progress.

Your job:

- Explain strengths
- Explain weaknesses
- Give recommendations for parents
- Keep it concise
- Return response in Uzbek language.
"""

    user_prompt = f"""
Goals count: {data['goals_count']}

Completed goals: {data['completed_goals']}

Skills count: {data['skills_count']}

Habits count: {data['habits_count']}

Latest assessment: {data['latest_assessment']}
"""

    return ask_ai(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        task_name="parent_summary"
    )