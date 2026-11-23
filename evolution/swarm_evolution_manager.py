class SwarmEvolutionManager:

    def __init__(self):

        self.generations = []

    def evaluate(
        self,
        swarm_score
    ):

        self.generations.append(
            swarm_score
        )

    def best_generation(self):

        if not self.generations:
            return None

        return max(
            self.generations
        )

    def trend(self):

        return self.generations
      
