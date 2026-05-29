from schemas.thinking_tools.skill_map import SkillMapRequest


def analyze_skill_map(data: SkillMapRequest):

    scores = {
        "communication": data.communication,
        "leadership": data.leadership,
        "creativity": data.creativity,
        "discipline": data.discipline,
        "teamwork": data.teamwork
    }

    strongest = max(scores, key=scores.get)
    weakest = min(scores, key=scores.get)

    return {
        "scores": scores,
        "strongest_skill": strongest,
        "weakest_skill": weakest
    }