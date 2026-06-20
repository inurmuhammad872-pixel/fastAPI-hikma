from services.ai.base_ai_service import ask_ai
import json


def generate_questions(category: str):

    system_prompt = """
You are an educational AI inside Hikma platform.

Generate exactly 5 questions.

Rules:

- Uzbek language
- Short questions
- Return ONLY JSON array
- No explanations

Example:

[
"question1",
"question2",
"question3",
"question4",
"question5"
]
"""

    user_prompt = f"""

Category:

{category}

"""

    result = ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="question_generator"
    )

    return json.loads(result)