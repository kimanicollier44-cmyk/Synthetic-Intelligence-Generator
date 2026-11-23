class StrategicWorldModel:

    def __init__(self):

        self.domains = {}

    def update(
        self,
        domain,
        state
    ):

        self.domains[
            domain
        ] = state

    def analyze(
        self,
        domain
    ):

        return self.domains.get(
            domain,
            {}
        )

    def snapshot(self):

        return self.domains
      
