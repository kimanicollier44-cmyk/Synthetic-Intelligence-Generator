class AgentSocietyManager:

    def __init__(self):

        self.groups = {}

    def create_group(
        self,
        name
    ):

        self.groups[name] = []

    def add_agent(
        self,
        group,
        agent
    ):

        self.groups.setdefault(
            group,
            []
        ).append(agent)

    def members(
        self,
        group
    ):

        return self.groups.get(
            group,
            []
        )
      
