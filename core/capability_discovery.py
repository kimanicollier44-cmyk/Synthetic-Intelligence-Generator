class CapabilityDiscovery:

    def __init__(self):

        self.capabilities = {}

    def register(
        self,
        name,
        description
    ):

        self.capabilities[
            name
        ] = description

    def discover(
        self,
        keyword=None
    ):

        if keyword is None:

            return self.capabilities

        return {

            name: desc

            for name, desc

            in self.capabilities.items()

            if keyword.lower()
            in desc.lower()
        }
      
