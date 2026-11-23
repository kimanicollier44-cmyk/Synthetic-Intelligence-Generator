class UncertaintyEstimator:

    def estimate(
        self,
        confidence_scores
    ):

        if not confidence_scores:
            return 1.0

        average = (
            sum(confidence_scores)
            / len(confidence_scores)
        )

        return round(
            1 - average,
            3
        )

    def classify(
        self,
        uncertainty
    ):

        if uncertainty < 0.2:
            return "low"

        if uncertainty < 0.5:
            return "medium"

        return "high"
      
