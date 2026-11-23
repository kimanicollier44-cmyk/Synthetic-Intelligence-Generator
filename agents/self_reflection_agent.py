class SelfReflectionAgent:

    def __init__(
        self,
        model
    ):

        self.model = model

    def reflect(
        self,
        output
    ):

        prompt = f"""
        Review output.

        Identify:

        - mistakes
        - assumptions
        - missing details
        - possible improvements

        Output:

        {output}
        """

        return self.model.generate(
            prompt
        )
      
