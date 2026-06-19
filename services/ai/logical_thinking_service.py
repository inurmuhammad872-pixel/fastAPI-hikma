from services.ai.base_ai_service import ask_ai


def evaluate_logical(question: str, answer: str):

    print("LOGICAL V2 IS WORKING")

    system_prompt = """
    You are an expert logical thinking evaluator.

    Evaluate:
    - logical consistency
    - reasoning quality
    - correctness
    - conclusion quality

    Give constructive feedback.
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
        task_name="logical"
    )