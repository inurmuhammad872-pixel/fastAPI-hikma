from schemas.thinking_tools.pdsa import PDSARequest
from services.ai.base_ai_service import ask_ai


def analyze_pdsa(data: PDSARequest):

    system_prompt = """
    You are an improvement cycle assistant using the PDSA framework.
    """

    user_prompt = f"""
    Goal:
    {data.goal}

    Problem:
    {data.current_problem}

    Generate:
    - Plan
    - Do
    - Study
    - Act
    """

    return ask_ai(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        task_name="cause_effect"
    )