class WorkflowMarketplace:

    def __init__(self):

        self.workflows = {}

    def publish(
        self,
        name,
        workflow
    ):

        self.workflows[
            name
        ] = workflow

    def get(
        self,
        name
    ):

        return self.workflows.get(
            name
        )

    def list_all(self):

        return list(
            self.workflows.keys()
        )
      
