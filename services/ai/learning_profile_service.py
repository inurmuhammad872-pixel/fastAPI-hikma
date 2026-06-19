class LearningProfileService:

    def build_profile(
        self,
        analyses: list
    ):
        logic_avg = sum(
            a.logic for a in analyses
        ) / len(analyses)

        evidence_avg = sum(
            a.evidence for a in analyses
        ) / len(analyses)

        return {
            "logic": logic_avg,
            "evidence": evidence_avg,
        }