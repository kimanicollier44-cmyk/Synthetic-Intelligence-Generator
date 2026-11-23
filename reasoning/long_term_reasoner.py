class LongTermReasoner:

    def __init__(
        self,
        model
    ):

        self.model = model

    def generate_strategy(
        self,
        objective,
        horizon="90 days"
    ):

        prompt = f"""
        Objective:
        {objective}

        Planning Horizon:
        {horizon}

        Produce:

        - milestones
        - dependencies
        - risks
        - checkpoints
        """

        return self.model.generate(
            prompt
        )
      
