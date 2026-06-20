AI_TASKS = {

    "logical": "openai",

    "cause_effect": "openai",

    "questioning": "openai",

    "five_why": "openai",

    "swot": "openai",

    "pareto": "openai",

    "pdsa": "openai",

    "decision_matrix": "openai",

    "creative": "openai",

    "critical": "openai",

    "conclusion": "openai",

    "parent_summary": "openai",

    "learning_profile": "openai",
}


def get_provider(task_name: str):

    return AI_TASKS.get(
        task_name,
        "openai"
    )