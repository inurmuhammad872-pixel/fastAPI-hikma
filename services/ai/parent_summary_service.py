class ParentSummaryService:

    def __init__(self, ai_service):
        self.ai_service = ai_service

    async def generate_summary(
        self,
        student_name: str,
        scores: dict
    ):
        prompt = f"""
        Student: {student_name}

        Scores:
        {scores}

        Write a short parent-friendly summary.
        """

        return await self.ai_service.generate(prompt)