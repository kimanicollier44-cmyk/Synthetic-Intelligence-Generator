class EmergentBehaviorDetector:

    def __init__(self):

        self.history = []

    def observe(
        self,
        event
    ):

        self.history.append(
            event
        )

    def detect_patterns(self):

        patterns = {}

        for event in self.history:

            patterns[event] = (
                patterns.get(
                    event,
                    0
                ) + 1
            )

        return {

            key: value

            for key, value

            in patterns.items()

            if value > 3
        }

    def report(self):

        return {

            "events":
            len(self.history),

            "patterns":
            self.detect_patterns()
        }
      
