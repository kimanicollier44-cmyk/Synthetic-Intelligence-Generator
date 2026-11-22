class AgentRegistry:

    def __init__(self):

        self.agents = {}

    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent

    def get(
        self,
        name
    ):

        return self.agents.get(
            name
        )

    def list_agents(
        self
    ):

        return list(
            self.agents.keys()
        )

    def execute(
        self,
        name,
        *args,
        **kwargs
    ):

        agent = self.get(
            name
        )

        if not agent:

            raise ValueError(
                f"Agent {name} "
                f"not found"
            )

        return agent.run(
            *args,
            **kwargs
        )
      
