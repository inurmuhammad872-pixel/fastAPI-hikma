from services.ai.base_ai_service import ask_ai


def generate_logical_questions(
    scenario
):

    system_prompt = """
You are an educational AI mentor inside Hikma.

Generate exactly 5 Socratic questions.

Rules:

- Ask only one logical question at a time.
- Questions must deepen reasoning.
- Questions must challenge assumptions.
- Questions must ask for evidence.
- Return only questions.
- Uzbek language.
"""

    user_prompt = f"""

Scenario:

{scenario}
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="logical"

    )


def analyze_logical_answers(

    scenario,

    answers

):

    system_prompt = """
You are an educational AI mentor.

Analyze student's logical reasoning.

Tasks:

- Evaluate reasoning

- Evaluate evidence

- Find weak points

- Give constructive feedback

- Give practical recommendations

Return Uzbek language.
"""

    user_prompt = f"""

Scenario:

{scenario}

Answers:

{answers}
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="logical"

    )

