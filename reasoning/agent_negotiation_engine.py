class AgentNegotiationEngine:

    def negotiate(
        self,
        proposals
    ):

        if not proposals:
            return None

        ranking = sorted(
            proposals,
            key=lambda x:
            x.get(
                "confidence",
                0
            ),
            reverse=True
        )

        winner = ranking[0]

        return {

            "selected": winner,

            "alternatives":
            ranking[1:]
        }
      
