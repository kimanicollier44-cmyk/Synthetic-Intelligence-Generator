from datetime import datetime


class SecurityAuditor:

    def __init__(self):

        self.events = []

    def record(
        self,
        actor,
        action,
        result
    ):

        self.events.append({

            "timestamp":
            datetime.utcnow().isoformat(),

            "actor":
            actor,

            "action":
            action,

            "result":
            result
        })

    def history(self):

        return self.events
