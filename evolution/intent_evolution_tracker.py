class IntentEvolutionTracker:

    def __init__(self):

        self.history = []

    def record(
        self,
        goal
    ):

        self.history.append(
            goal
        )

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def evolution_path(self):

        return self.history
      
