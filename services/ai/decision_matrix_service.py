from schemas.thinking_tools.decision_matrix import DecisionMatrixRequest
from services.ai.base_ai_service import ask_ai


def analyze_decision_matrix(data: DecisionMatrixRequest):

    system_prompt = """
    You are a strategic decision-making assistant.
    """

    user_prompt = f"""
    Decision:
    {data.decision}

    Options:
    {", ".join(data.options)}

    Criteria:
    {", ".join(data.criteria)}

    Analyze each option and recommend the best one.
    """

    return ask_ai(system_prompt, user_prompt)