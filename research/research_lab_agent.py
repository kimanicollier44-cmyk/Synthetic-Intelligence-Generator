class ResearchLabAgent:

    def __init__(
        self,
        researcher,
        simulator,
        validator
    ):

        self.researcher = researcher
        self.simulator = simulator
        self.validator = validator

    def investigate(
        self,
        topic
    ):

        findings = (
            self.researcher
            .investigate(topic)
        )

        validation = (
            self.validator
            .validate(findings)
        )

        return {

            "topic": topic,
            "findings": findings,
            "validation": validation
        }
      
