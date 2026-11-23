class ConsensusEngine:

    def build_consensus(
        self,
        responses
    ):

        rankings = {}

        for response in responses:

            score = len(
                response
            )

            rankings[
                response
            ] = score

        winning = max(
            rankings,
            key=rankings.get
        )

        return {
            "winner": winning,
            "scores": rankings
        }
      
