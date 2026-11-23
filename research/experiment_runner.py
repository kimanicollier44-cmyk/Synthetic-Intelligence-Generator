class ExperimentRunner:

    def run(
        self,
        hypothesis,
        trials
    ):

        results = []

        for trial in trials:

            results.append({

                "hypothesis":
                hypothesis,

                "trial":
                trial,

                "status":
                "completed"
            })

        return results

    def summarize(
        self,
        results
    ):

        return {

            "experiments":
            len(results),

            "successful":
            len(results)
        }
      
