class CoderAgent:

    def __init__(self, model):
        self.model = model

    def generate(
        self,
        request,
        plan
    ):

        prompt = f"""
        Objective:

        {request}

        Plan:

        {plan}

        Generate the best solution.
        """

        return self.model.generate(prompt)
      
