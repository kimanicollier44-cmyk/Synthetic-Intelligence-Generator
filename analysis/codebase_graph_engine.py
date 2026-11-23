class CodebaseGraphEngine:

    def __init__(self):

        self.modules = {}
        self.dependencies = []

    def add_module(
        self,
        name
    ):

        self.modules[name] = []

    def add_dependency(
        self,
        source,
        target
    ):

        self.dependencies.append({

            "source": source,

            "target": target
        })

    def dependency_map(self):

        graph = {}

        for edge in self.dependencies:

            graph.setdefault(
                edge["source"],
                []
            ).append(
                edge["target"]
            )

        return graph
      
