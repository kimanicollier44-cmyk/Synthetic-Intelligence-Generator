class FederatedMemory:

    def __init__(self):

        self.stores = {}

    def register_store(
        self,
        name,
        memory_store
    ):

        self.stores[name] = memory_store

    def save(
        self,
        key,
        value
    ):

        for store in self.stores.values():

            store.save(
                key,
                value
            )

    def search(
        self,
        query
    ):

        results = []

        for store in self.stores.values():

            if hasattr(
                store,
                "search"
            ):

                results.extend(
                    store.search(
                        query
                    )
                )

        return results
      
