class CognitiveSecurityLayer:

    def __init__(self):

        self.blocked_actions = set()

    def block(
        self,
        action
    ):

        self.blocked_actions.add(
            action
        )

    def allowed(
        self,
        action
    ):

        return (
            action
            not in
            self.blocked_actions
        )

    def authorize(
        self,
        action,
        callback
    ):

        if not self.allowed(
            action
        ):

            raise PermissionError(
                "Action denied"
            )

        return callback()
      
