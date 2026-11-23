class AgentGovernor:

    def __init__(self):

        self.rules = []

    def add_rule(
        self,
        rule
    ):

        self.rules.append(
            rule
        )

    def evaluate(
        self,
        action
    ):

        for rule in self.rules:

            if not rule(action):

                return False

        return True

    def authorize(
        self,
        action,
        callback
    ):

        if self.evaluate(
            action
        ):

            return callback()

        raise PermissionError(
            "Action blocked"
        )
      
