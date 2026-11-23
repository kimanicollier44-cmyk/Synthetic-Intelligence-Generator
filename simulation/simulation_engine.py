class SimulationEngine:

    def simulate(
        self,
        options
    ):

        outcomes = []

        for option in options:

            outcomes.append({

                "option":
                option,

                "score":
                len(str(option))
            })

        return sorted(

            outcomes,

            key=lambda x:
            x["score"],

            reverse=True
        )
      
