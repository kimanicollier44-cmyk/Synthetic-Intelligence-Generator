class MetaReasoningEngine:

    def evaluate_reasoning(
        self,
        reasoning_trace
    ):

        strengths = []
        weaknesses = []

        for step in reasoning_trace:

            if len(str(step)) > 20:
                strengths.append(step)
            else:
                weaknesses.append(step)

        return {
            "strengths": strengths,
            "weaknesses": weaknesses
        }

    def improve(
        self,
        reasoning_trace
    ):

        return {
            "original": reasoning_trace,
            "recommendation":
            "add verification stage"
        }
      
