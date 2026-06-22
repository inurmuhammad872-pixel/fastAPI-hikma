from schemas.thinking_tools.pdsa import PDSARequest

from services.ai.base_ai_service import ask_ai


def analyze_pdsa(
    data: PDSARequest
):

    system_prompt = """
You are an educational AI mentor inside Hikma platform.

Analyze using the PDSA framework.

Tasks:

- Create Plan

- Create Do

- Create Study

- Create Act

Rules:

- Return Uzbek language.

- Keep the response concise.

- Give practical advice.
"""

    user_prompt = f"""

Goal:

{data.goal}

Current Problem:

{data.current_problem}

Generate this structure:

Plan:

Do:

Study:

Act:
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="pdsa"
    )