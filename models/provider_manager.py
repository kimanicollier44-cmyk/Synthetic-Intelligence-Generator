class ProviderManager:

    def __init__(self):

        self.active = None

    def set_active(
        self,
        provider
    ):

        self.active = provider

    def run(
        self,
        prompt
    ):

        if not self.active:

            raise RuntimeError(
                "No active provider"
            )

        return self.active.generate(
            prompt
        )
      
