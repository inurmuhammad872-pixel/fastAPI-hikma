from services.ai.base_ai_service import ask_ai


def generate_questions(
    scenario
):

    system_prompt = """
You are an educational AI mentor inside Hikma platform.

Generate exactly 5 Socratic questions.

Rules:

- Return Uzbek language.

- Ask one question at a time.

- Help deepen the student's thinking.
"""

    user_prompt = f"""

Scenario:

{scenario}

Generate 5 questions.
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="logical"
    )


def analyze_answers(

    scenario,

    answers

):

    system_prompt = """
You are an educational AI mentor.

Analyze the student's thinking.

Tasks:

- Find strengths

- Find weak points

- Give recommendations

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


def generate_feedback(

    scenario,

    observe,

    reason,

    evidence,

    alternative,

    conclusion

):

    system_prompt = """
You are an educational AI mentor.

Analyze final conclusion.

Tasks:

- Evaluate logic

- Evaluate evidence

- Evaluate alternative thinking

- Give final feedback

Return Uzbek language.
"""

    user_prompt = f"""

Scenario:

{scenario}

Observation:

{observe}

Reason:

{reason}

Evidence:

{evidence}

Alternative:

{alternative}

Conclusion:

{conclusion}
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="logical"
    )