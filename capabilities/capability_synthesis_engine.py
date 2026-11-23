class CapabilitySynthesisEngine:

    def combine(
        self,
        capabilities
    ):

        synthesized = {

            "count":
            len(capabilities),

            "capabilities":
            capabilities
        }

        return synthesized

    def create_skill(
        self,
        name,
        requirements
    ):

        return {

            "skill":
            name,

            "requirements":
            requirements
        }
      
