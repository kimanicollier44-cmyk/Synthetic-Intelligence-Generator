class LongHorizonPlanner:

    def create_roadmap(
        self,
        objective,
        quarters=4
    ):

        roadmap = []

        for quarter in range(
            1,
            quarters + 1
        ):

            roadmap.append({

                "quarter":
                quarter,

                "objective":
                objective,

                "milestone":
                f"Phase {quarter}"
            })

        return roadmap
      
