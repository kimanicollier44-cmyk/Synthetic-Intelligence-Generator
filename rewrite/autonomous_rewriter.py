class AutonomousRewriter:

    def __init__(
        self,
        model
    ):

        self.model = model

    def improve(
        self,
        content
    ):

        prompt = f"""
        Rewrite and improve:

        {content}

        Goals:
        - clarity
        - efficiency
        - maintainability
        """

        return self.model.generate(
            prompt
        )

    def refactor_plan(
        self,
        code
    ):

        return {

            "target": code,

            "action":
            "refactor"
        }
      
