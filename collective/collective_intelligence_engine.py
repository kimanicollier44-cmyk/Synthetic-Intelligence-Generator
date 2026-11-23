class CollectiveIntelligenceEngine:

    def aggregate(
        self,
        agent_outputs
    ):

        return {

            "contributors":
            len(agent_outputs),

            "knowledge":
            agent_outputs
        }

    def synthesize(
        self,
        agent_outputs
    ):

        combined = []

        for output in agent_outputs:

            combined.append(
                output
            )

        return combined
      
