class CostTracker:

    def __init__(self):

        self.total_cost = 0.0

    def record(
        self,
        amount
    ):

        self.total_cost += amount

    def current_cost(self):

        return round(
            self.total_cost,
            4
        )

    def reset(self):

        self.total_cost = 0.0
