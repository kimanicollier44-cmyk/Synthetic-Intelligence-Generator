class AutonomousTeamBuilder:

    def build_team(
        self,
        objective
    ):

        return [

            {
                "role":
                "planner"
            },

            {
                "role":
                "researcher"
            },

            {
                "role":
                "analyst"
            },

            {
                "role":
                "reviewer"
            }
        ]

    def assign(
        self,
        task,
        team
    ):

        return {

            "task": task,

            "team": team
        }
      
