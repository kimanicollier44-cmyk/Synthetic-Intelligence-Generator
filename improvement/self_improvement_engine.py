class SelfImprovementEngine:

    def __init__(self):

        self.improvements = []

    def evaluate(
        self,
        metric,
        current,
        target
    ):

        gap = target - current

        recommendation = {

            "metric": metric,

            "current": current,

            "target": target,

            "gap": gap
        }

        self.improvements.append(
            recommendation
        )

        return recommendation

    def roadmap(self):

        return self.improvements
      
