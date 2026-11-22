class WebSearchAgent:

    def __init__(
        self,
        browser_agent,
        model
    ):

        self.browser = (
            browser_agent
        )

        self.model = model

    def research(
        self,
        topic
    ):

        search_results = (
            self.browser.browse(
                topic
            )
        )

        prompt = f"""
        Topic:
        {topic}

        Search Results:
        {search_results}

        Create a concise
        research summary.
        """

        return self.model.generate(
            prompt
        )
      
