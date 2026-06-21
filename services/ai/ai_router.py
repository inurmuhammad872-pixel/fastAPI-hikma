AI_TASKS = {

    # Thinking

    "logical": "openai",

    "cause_effect": "openai",

    "questioning": "openai",

    "creative": "openai",

    "critical": "openai",

    "conclusion": "openai",

    # Thinking Tools

    "five_why": "openai",

    "swot": "openai",

    "pareto": "openai",

    "pdsa": "openai",

    "decision_matrix": "openai",

    # Growth

    "question_generator": "openai",

    # Reports

    "parent_summary": "claude",

    "learning_profile": "claude",

}


def get_provider(task_name: str):

    return AI_TASKS.get(
        task_name,
        "openai"
    )