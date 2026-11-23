class ModelVotingEngine:

    def vote(
        self,
        candidates
    ):

        if not candidates:

            return None

        scores = {}

        for item in candidates:

            score = item.get(
                "score",
                0
            )

            scores[
                item["provider"]
            ] = score

        winner = max(
            scores,
            key=scores.get
        )

        return {

            "winner":
            winner,

            "scores":
            scores
        }
      
