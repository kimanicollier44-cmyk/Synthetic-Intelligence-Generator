class ReasoningGenome:

    def __init__(self):

        self.genes = []

    def add_gene(
        self,
        strategy
    ):

        self.genes.append(
            strategy
        )

    def sequence(self):

        return self.genes

    def combine(
        self,
        other_genome
    ):

        return (
            self.genes +
            other_genome.genes
        )
      
