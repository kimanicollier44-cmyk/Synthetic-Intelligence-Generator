class AutonomousPlanner:

    def __init__(
        self,
        model
    ):

        self.model = model

    def create_plan(
        self,
        objective
    ):

        prompt = f"""
        Objective:

        {objective}

        Create:

        1. Goals
        2. Milestones
        3. Risks
        4. Actions
        5. Success metrics
        """

        return self.model.generate(
            prompt
        )

    def refine(
        self,
        objective,
        previous_result
    ):

        prompt = f"""
        Objective:
        {objective}

        Previous Result:
        {previous_result}

        Improve the plan.
        """

        return self.model.generate(
            prompt
        )
      
