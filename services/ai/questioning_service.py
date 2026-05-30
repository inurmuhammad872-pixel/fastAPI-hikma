from services.ai.base_ai_service import ask_ai


def evaluate_questioning(question: str, answer: str):

    system_prompt = """
    You are an expert questioning skills evaluator.

    Evaluate:
    - curiosity
    - depth
    - relevance
    - critical inquiry
    """

    user_prompt = f"""
    Topic:
    {question}

    Student Questions:
    {answer}
    """

    return ask_ai(system_prompt, user_prompt)