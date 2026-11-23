class TrustManager:

    def __init__(self):

        self.scores = {}

    def set_score(
        self,
        source,
        score
    ):

        self.scores[source] = score

    def score(
        self,
        source
    ):

        return self.scores.get(
            source,
            0.0
        )

    def trusted(
        self,
        source,
        threshold=0.7
    ):

        return (
            self.score(source)
            >= threshold
        )
      
