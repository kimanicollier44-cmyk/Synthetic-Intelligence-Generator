class BrowserAgent:

    def __init__(
        self,
        search_provider
    ):

        self.search_provider = (
            search_provider
        )

    def browse(
        self,
        query
    ):

        pages = (
            self.search_provider
            .search(query)
        )

        return {

            "query": query,

            "results": pages
        }
      
