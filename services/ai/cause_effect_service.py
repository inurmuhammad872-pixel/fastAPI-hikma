from services.ai.base_ai_service import ask_ai


def evaluate_cause_effect(question: str, answer: str):

    system_prompt = """
    You are an expert cause and effect evaluator.

    Evaluate:
    - cause identification
    - effect identification
    - relationship accuracy
    - reasoning quality
    """

    user_prompt = f"""
    Question:
    {question}

    Student Answer:
    {answer}
    """

    return ask_ai(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        task_name="cause_effect"
    )