class AgentTrainingManager:

    def __init__(self):

        self.agents = {}

    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent

    def train(
        self,
        dataset
    ):

        report = {}

        for name, agent in (

            self.agents.items()

        ):

            if hasattr(
                agent,
                "train"
            ):

                report[name] = (

                    agent.train(
                        dataset
                    )
                )

        return report
      
