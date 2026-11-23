class GraphMemory:

    def __init__(self):

        self.nodes = {}
        self.edges = []

    def add_node(
        self,
        node_id,
        payload
    ):

        self.nodes[node_id] = payload

    def link(
        self,
        source,
        target,
        relation
    ):

        self.edges.append({

            "source": source,

            "target": target,

            "relation": relation
        })

    def neighbors(
        self,
        node_id
    ):

        return [

            edge

            for edge in self.edges

            if edge["source"] == node_id
        ]
      
