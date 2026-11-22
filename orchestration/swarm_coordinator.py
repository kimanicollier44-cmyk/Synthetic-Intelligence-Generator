class SwarmCoordinator:

    def __init__(self):

        self.agents = {}

    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent

    def broadcast(
        self,
        task
    ):

        results = {}

        for name, agent in (
            self.agents.items()
        ):

            try:

                results[name] = (
                    agent.run(task)
                )

            except Exception as ex:

                results[name] = (
                    str(ex)
                )

        return results

    def collaborative_run(
        self,
        task
    ):

        outputs = (
            self.broadcast(task)
        )

        return {

            "task": task,

            "contributors":
            list(
                outputs.keys()
            ),

            "results":
            outputs
        }
      
