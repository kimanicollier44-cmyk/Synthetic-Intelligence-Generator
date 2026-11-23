class NeuralMemoryEngine:

    def __init__(self):

        self.memories = []

    def store(
        self,
        memory
    ):

        self.memories.append(
            memory
        )

    def retrieve(
        self,
        query
    ):

        matches = []

        for memory in self.memories:

            if query.lower() in str(
                memory
            ).lower():

                matches.append(
                    memory
                )

        return matches

    def consolidate(self):

        return list(
            set(
                map(str, self.memories)
            )
        )
