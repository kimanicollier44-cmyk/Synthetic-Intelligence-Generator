class AdaptivePersonaManager:

    def __init__(self):

        self.personas = {}

    def register(
        self,
        name,
        traits
    ):

        self.personas[name] = traits

    def get(
        self,
        name
    ):

        return self.personas.get(
            name
        )

    def select(
        self,
        context
    ):

        if "research" in context:

            return "researcher"

        if "coding" in context:

            return "engineer"

        return "generalist"
      
