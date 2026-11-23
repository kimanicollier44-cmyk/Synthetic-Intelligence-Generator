class KnowledgeGraphBuilder:

    def __init__(self):

        self.nodes = set()
        self.edges = []

    def add_fact(
        self,
        subject,
        relation,
        object_
    ):

        self.nodes.add(subject)

        self.nodes.add(object_)

        self.edges.append({

            "subject": subject,

            "relation": relation,

            "object": object_
        })

    def graph(self):

        return {

            "nodes":
            list(self.nodes),

            "edges":
            self.edges
        }
      
