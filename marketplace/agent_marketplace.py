class AgentMarketplace:

    def __init__(self):

        self.catalog = {}

    def publish(
        self,
        name,
        metadata
    ):

        self.catalog[name] = metadata

    def search(
        self,
        keyword
    ):

        results = {}

        for name, data in (
            self.catalog.items()
        ):

            if keyword.lower() in (
                str(data).lower()
            ):
                results[name] = data

        return results

    def list_agents(self):

        return self.catalog
      
