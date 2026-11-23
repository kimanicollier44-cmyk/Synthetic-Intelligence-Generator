class AutonomousExecutor:

    def __init__(
        self,
        registry
    ):

        self.registry = registry

    def execute_plan(
        self,
        plan
    ):

        results = []

        for step in plan:

            agent_name = step[
                "agent"
            ]

            payload = step[
                "payload"
            ]

            agent = (
                self.registry.get(
                    agent_name
                )
            )

            if not agent:
                continue

            result = agent.run(
                payload
            )

            results.append(
                result
            )

        return results
