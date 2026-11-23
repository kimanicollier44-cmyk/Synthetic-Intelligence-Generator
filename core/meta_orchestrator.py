class MetaOrchestrator:

    def __init__(
        self,
        universal_orchestrator,
        architecture_manager,
        security_layer
    ):

        self.universal = (
            universal_orchestrator
        )

        self.architecture = (
            architecture_manager
        )

        self.security = (
            security_layer
        )

    def execute(
        self,
        objective
    ):

        if not self.security.allowed(
            "execute"
        ):

            raise PermissionError()

        return (
            self.universal
            .execute(
                objective
            )
        )

    def oversee(self):

        return {

            "architecture":
            self.architecture.status(),

            "security":
            "active"
        }
      
