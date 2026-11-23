class AdaptiveRouter:

    def __init__(
        self,
        benchmark,
        providers
    ):

        self.benchmark = benchmark
        self.providers = providers

    def choose_provider(
        self,
        task_type
    ):

        if task_type == "coding":
            return "openai"

        if task_type == "research":
            return "gemini"

        if task_type == "analysis":
            return "anthropic"

        return "gemini"

    def execute(
        self,
        task_type,
        prompt
    ):

        provider = (
            self.choose_provider(
                task_type
            )
        )

        return self.providers[
            provider
        ].generate(prompt)
      
