class GraphReasoner:

    def __init__(
        self,
        graph_memory
    ):

        self.graph = graph_memory

    def find_paths(
        self,
        start
    ):

        return self.graph.neighbors(
            start
        )

    def reason(
        self,
        entity
    ):

        relations = (
            self.find_paths(
                entity
            )
        )

        return {

            "entity": entity,

            "relations":
            relations
        }
      
