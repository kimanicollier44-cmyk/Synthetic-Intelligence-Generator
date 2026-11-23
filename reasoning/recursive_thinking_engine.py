class RecursiveThinkingEngine:

    def __init__(
        self,
        model
    ):

        self.model = model

    def think(
        self,
        problem,
        depth=3
    ):

        result = problem

        for level in range(
            depth
        ):

            prompt = f"""
            Analyze:

            {result}

            Improve reasoning.
            Depth:
            {level + 1}
            """

            result = (
                self.model.generate(
                    prompt
                )
            )

        return result
      
