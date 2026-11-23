class CausalInferenceEngine:

    def infer(
        self,
        observations
    ):

        relationships = []

        for record in observations:

            if "cause" in record and \
               "effect" in record:

                relationships.append({

                    "cause":
                    record["cause"],

                    "effect":
                    record["effect"]
                })

        return relationships

    def explain(
        self,
        cause,
        effect
    ):

        return (
            f"{cause} may "
            f"influence "
            f"{effect}"
        )
      
