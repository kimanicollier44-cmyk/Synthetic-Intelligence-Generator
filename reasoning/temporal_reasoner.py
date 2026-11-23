from datetime import datetime


class TemporalReasoner:

    def evaluate_timeline(
        self,
        events
    ):

        ordered = sorted(
            events,
            key=lambda x:
            x["timestamp"]
        )

        return ordered

    def next_event(
        self,
        events
    ):

        now = datetime.utcnow()

        future = [

            event

            for event in events

            if event["timestamp"] > now
        ]

        return future[0] if future else None
      
