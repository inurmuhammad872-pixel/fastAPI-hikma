from schemas.thinking_tools.five_why import FiveWhyRequest

from services.ai.base_ai_service import ask_ai


def analyze_five_why(
    data: FiveWhyRequest
):

    system_prompt = """
You are an expert root cause analysis mentor inside Hikma platform.

Your task is to perform a Five Why analysis.

Rules:

- Generate exactly 5 why steps.
- Find the root cause.
- Give one practical recommendation.
- Return the answer in Uzbek language.
- Keep the answer concise and clear.
"""

    user_prompt = f"""
Problem:

{data.problem}

Return using this exact structure.

1. Why:
...

2. Why:
...

3. Why:
...

4. Why:
...

5. Why:
...

Root Cause:
...

Recommendation:
...
"""

    return ask_ai(

        system_prompt=system_prompt,

        user_prompt=user_prompt,

        task_name="five_why"
    )