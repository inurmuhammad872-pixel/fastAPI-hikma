from schemas.thinking_tools.pareto import ParetoRequest
from services.ai.base_ai_service import ask_ai


def analyze_pareto(data: ParetoRequest):

    system_prompt = """
    You are an expert productivity strategist.

    Apply the Pareto 80/20 principle.
    """

    user_prompt = f"""
    Goal:
    {data.goal}

    Activities:
    {", ".join(data.activities)}

    Identify:
    - Top 20% highest impact activities
    - Low value activities
    - Recommendation
    """

    return ask_ai(system_prompt, user_prompt)