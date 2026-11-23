class ScientificReasoner:

    def formulate_hypothesis(
        self,
        observation
    ):

        return (
            f"Hypothesis based on "
            f"{observation}"
        )

    def design_experiment(
        self,
        hypothesis
    ):

        return {

            "hypothesis":
            hypothesis,

            "steps": [

                "collect data",

                "run experiment",

                "analyze results"
            ]
        }

    def evaluate(
        self,
        results
    ):

        return {

            "results": results,

            "status":
            "evaluated"
        }
      
