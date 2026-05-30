# services/ai/logical_thinking_service.py

from services.ai.base_ai_service import ask_ai


def evaluate_logical(question: str, answer: str):

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

    return ask_ai(system_prompt, user_prompt)