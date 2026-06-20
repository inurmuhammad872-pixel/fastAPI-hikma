from services.ai.base_ai_service import ask_ai


def generate_learning_profile(
    data
):

    system_prompt = """
You are an educational AI mentor inside Hikma platform.

Analyze the student profile.

Tasks:

- Find strengths

- Find weaknesses

- Find learning style

- Find growth areas

- Give practical advice

Return response in Uzbek language.

Keep response concise.
"""

    user_prompt = f"""
Goals:

{data['goals']}


Skills:

{data['skills']}


Habits:

{data['habits']}


Self Assessment:

{data['assessment']}
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="learning_profile"
    )