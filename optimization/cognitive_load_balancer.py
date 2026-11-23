class CognitiveLoadBalancer:

    def distribute(
        self,
        tasks,
        agents
    ):

        assignments = {}

        for index, task in enumerate(tasks):

            agent = agents[
                index % len(agents)
            ]

            assignments.setdefault(
                agent,
                []
            ).append(task)

        return assignments

    def utilization(
        self,
        assignments
    ):

        return {

            agent: len(tasks)

            for agent, tasks

            in assignments.items()
        }
      
