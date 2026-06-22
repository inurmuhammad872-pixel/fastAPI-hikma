from services.ai.base_ai_service import ask_ai


def generate_five_why_questions(
    problem
):

    system_prompt = """
You are an educational AI mentor inside Hikma platform.

Generate exactly 5 consecutive why questions.

Rules:

- Each question must depend on the previous one.

- Return Uzbek language.

- Return only numbered questions.
"""

    user_prompt = f"""

Problem:

{problem}
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="five_why"
    )


def analyze_five_why(
    problem,
    answers
):

    formatted_answers = "\n".join(

        [

            f"Why {i+1}: {answer}"

            for i, answer in enumerate(

                answers

            )
        ]
    )

    system_prompt = """
You are an educational AI mentor inside Hikma platform.

Analyze the user's Five Why answers.

Tasks:

- Find the root cause

- Give constructive feedback

- Create exactly 3 action steps

Return Uzbek language.

Keep the answer concise.
"""

    user_prompt = f"""

Problem:

{problem}

User answers:

{formatted_answers}

Generate:

Root Cause:

Feedback:

Action Plan:
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="five_why"
    )