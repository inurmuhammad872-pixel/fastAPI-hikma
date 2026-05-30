from services.ai.base_ai_service import ask_ai


def evaluate_creative(question: str, answer: str):

    system_prompt = """
    You are an expert creative thinking evaluator.

    Evaluate:
    - originality
    - flexibility
    - uniqueness
    - innovation

    Give constructive feedback.
    """

    user_prompt = f"""
    Question:
    {question}

    Student Answer:
    {answer}
    """

    return ask_ai(system_prompt, user_prompt)