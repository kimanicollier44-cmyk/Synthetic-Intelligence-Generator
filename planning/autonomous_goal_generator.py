import uuid


class AutonomousGoalGenerator:

    def generate(
        self,
        domain
    ):

        return {

            "id":
            str(
                uuid.uuid4()
            ),

            "domain":
            domain,

            "goal":
            f"Improve {domain}"
        }

    def prioritize(
        self,
        goals
    ):

        return sorted(
            goals,
            key=lambda x:
            x["goal"]
        )
      
