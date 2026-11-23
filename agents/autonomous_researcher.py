class AutonomousResearcher:

    def __init__(
        self,
        search_agent,
        reflection_agent
    ):

        self.search = search_agent
        self.reflect = (
            reflection_agent
        )

    def investigate(
        self,
        topic,
        iterations=3
    ):

        results = []

        current_topic = topic

        for _ in range(iterations):

            report = (
                self.search.research(
                    current_topic
                )
            )

            review = (
                self.reflect.reflect(
                    report
                )
            )

            results.append({

                "report": report,

                "review": review
            })

        return results
      
