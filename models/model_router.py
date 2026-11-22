class ModelRouter:

    def __init__(self):

        self.providers = {}

    def register_provider(
        self,
        name,
        provider
    ):

        self.providers[name] = provider

    def route(
        self,
        provider_name,
        prompt
    ):

        provider = (
            self.providers.get(
                provider_name
            )
        )

        if provider is None:

            raise ValueError(
                "Provider unavailable"
            )

        return provider.generate(
            prompt
        )
      
