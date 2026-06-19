class RecommendationService:

    def recommend(
        self,
        profile: dict
    ):
        if profile["logic"] < 50:
            return "logical_thinking"

        if profile["evidence"] < 50:
            return "cause_effect"

        return "critical_thinking"