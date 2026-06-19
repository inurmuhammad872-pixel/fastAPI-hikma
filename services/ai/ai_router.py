AI_TASKS = {

    "logical": "gemini",

    "cause_effect": "gemini",

    "questioning": "gemini",

    "five_why": "gemini",

    "swot": "gemini",

    "pareto": "gemini",

    "pdsa": "gemini",

    "decision_matrix": "gemini",

    "creative": "openai",

    "critical": "openai",

    "conclusion": "openai",

    "parent_summary": "claude",

    "learning_profile": "claude",
}


def get_provider(task_name: str):

    return AI_TASKS.get(
        task_name,
        "openai"
    )