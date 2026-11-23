class ReinforcementLoop:

    def __init__(self):

        self.history = []

    def record(
        self,
        action,
        reward
    ):

        self.history.append({

            "action": action,

            "reward": reward
        })

    def average_reward(self):

        if not self.history:
            return 0

        total = sum(
            item["reward"]
            for item in self.history
        )

        return total / len(
            self.history
        )

    def best_action(self):

        if not self.history:
            return None

        return max(
            self.history,
            key=lambda x:
            x["reward"]
        )
      
