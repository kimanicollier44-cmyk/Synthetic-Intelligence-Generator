from collections import defaultdict


class MetricsCollector:

    def __init__(self):

        self.metrics = defaultdict(
            int
        )

    def increment(
        self,
        metric_name
    ):

        self.metrics[
            metric_name
        ] += 1

    def record_tokens(
        self,
        count
    ):

        self.metrics[
            "tokens"
        ] += count

    def snapshot(self):

        return dict(
            self.metrics
        )
      
