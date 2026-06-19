class ConfidenceService:

    def evaluate(
        self,
        analysis: dict
    ):
        filled = len(
            [v for v in analysis.values() if v]
        )

        return round(
            filled / len(analysis),
            2
        )