class ModelBenchmark:

    def __init__(self):

        self.records = {}

    def record(
        self,
        provider,
        latency,
        score
    ):

        self.records.setdefault(
            provider,
            []
        ).append({

            "latency": latency,
            "score": score
        })

    def average_score(
        self,
        provider
    ):

        data = self.records.get(
            provider,
            []
        )

        if not data:
            return 0

        return sum(
            x["score"]
            for x in data
        ) / len(data)
      
