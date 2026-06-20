from services.ai.base_ai_service import ask_ai


def analyze_swot(
    topic,
    strengths,
    weaknesses,
    opportunities,
    threats
):

    system_prompt = """
    You are an expert SWOT analyst.

    Analyze the SWOT information.

    Give actionable recommendations.
    """

    user_prompt = f"""
    Topic: {topic}

    Strengths:
    {strengths}

    Weaknesses:
    {weaknesses}

    Opportunities:
    {opportunities}

    Threats:
    {threats}
    """

    return ask_ai(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        task_name="swot"
    )