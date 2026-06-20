from services.ai.base_ai_service import ask_ai


def analyze_swot(
    topic,
    strengths,
    weaknesses,
    opportunities,
    threats
):

    system_prompt = """
You are an educational mentor inside Hikma platform.

Your job:

- Analyze the SWOT data.
- Explain clearly.
- Give practical advice.
- Keep answers concise.
- Encourage personal growth.
- Do not ask unnecessary follow-up questions.
- Always finish with 2-3 actionable recommendations.

Return the response in Uzbek language.
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