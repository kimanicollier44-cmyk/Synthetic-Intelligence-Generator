class EpistemicValidator:

    def assess(
        self,
        claim,
        evidence_count
    ):

        if evidence_count >= 3:

            confidence = "high"

        elif evidence_count >= 1:

            confidence = "medium"

        else:

            confidence = "low"

        return {

            "claim": claim,

            "confidence":
            confidence
        }

    def requires_review(
        self,
        assessment
    ):

        return (
            assessment["confidence"]
            == "low"
        )
      
