from schemas.thinking_tools.five_why import FiveWhyRequest
from services.ai.base_ai_service import ask_ai


def analyze_five_why(data: FiveWhyRequest):

    system_prompt = """
    You are an expert root-cause analysis assistant.

    Analyze the user's problem using the 5 Why method.

    Return concise reasoning.
    """

    user_prompt = f"""
    Problem:
    {data.problem}

    Generate:
    - Why 1
    - Why 2
    - Why 3
    - Why 4
    - Root Cause
    - Final Conclusion
    """

    return ask_ai(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        task_name="cause_effect"
    )