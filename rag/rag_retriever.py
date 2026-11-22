class RagRetriever:

    def __init__(
        self,
        vector_store
    ):

        self.store = vector_store

    def retrieve(
        self,
        query,
        limit=5
    ):

        memories = self.store.load_memories()

        matches = []

        for item in memories:

            text = item.get(
                "text",
                ""
            )

            if query.lower() in text.lower():

                matches.append(
                    text
                )

        return matches[:limit]
      
