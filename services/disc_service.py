from schemas.thinking_tools.disc import DISCRequest


def analyze_disc(data: DISCRequest):

    scores = {
        "D": data.dominance,
        "I": data.influence,
        "S": data.steadiness,
        "C": data.conscientiousness
    }

    personality = max(scores, key=scores.get)

    return {
        "personality_type": personality,
        "scores": scores
    }