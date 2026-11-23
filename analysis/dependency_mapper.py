class DependencyMapper:

    def __init__(self):

        self.map = {}

    def register(
        self,
        module,
        dependency
    ):

        self.map.setdefault(
            module,
            []
        ).append(
            dependency
        )

    def dependencies(
        self,
        module
    ):

        return self.map.get(
            module,
            []
        )

    def export(self):

        return dict(
            self.map
        )
      
