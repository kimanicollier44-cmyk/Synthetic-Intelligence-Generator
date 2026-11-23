class ConsciousnessMonitor:

    def __init__(self):

        self.events = []

    def observe(
        self,
        subsystem,
        state
    ):

        self.events.append({

            "subsystem":
            subsystem,

            "state":
            state
        })

    def snapshot(self):

        return {

            "observations":
            len(self.events),

            "events":
            self.events[-100:]
        }

    def summarize(self):

        return {

            "active_systems":
            len(set(

                event["subsystem"]

                for event in self.events
            ))
        }
      
