class ExpertAgentManager:

    def __init__(self):

        self.experts = {}

    def register(
        self,
        domain,
        agent
    ):

        self.experts[
            domain
        ] = agent

    def get_expert(
        self,
        domain
    ):

        return self.experts.get(
            domain
        )

    def dispatch(
        self,
        domain,
        task
    ):

        agent = self.get_expert(
            domain
        )

        if not agent:
            return None

        return agent.run(task)
      
