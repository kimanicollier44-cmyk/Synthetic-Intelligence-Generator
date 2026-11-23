class DistributedReasoning:

    def __init__(
        self,
        agents
    ):

        self.agents = agents

    def solve(
        self,
        problem
    ):

        outputs = []

        for agent in self.agents:

            outputs.append(

                agent.run(
                    problem
                )
            )

        return outputs

    def aggregate(
        self,
        solutions
    ):

        return {

            "count":
            len(solutions),

            "solutions":
            solutions
        }
      
