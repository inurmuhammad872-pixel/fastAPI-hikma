from services.ai.base_ai_service import ask_ai


def evaluate_conclusion(question: str, answer: str):

    system_prompt = """
    You are an expert conclusion-making evaluator.

    Evaluate:
    - reasoning
    - evidence usage
    - conclusion quality
    - clarity
    """

    user_prompt = f"""
    Question:
    {question}

    Student Answer:
    {answer}
    """

    return ask_ai(system_prompt, user_prompt)