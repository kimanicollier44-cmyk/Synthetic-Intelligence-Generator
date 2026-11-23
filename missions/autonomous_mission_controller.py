class AutonomousMissionController:

    def __init__(
        self,
        planner,
        executor
    ):

        self.planner = planner
        self.executor = executor

    def launch(
        self,
        mission
    ):

        plan = (
            self.planner
            .create_roadmap(
                mission
            )
        )

        return {

            "mission":
            mission,

            "plan":
            plan
        }

    def execute(
        self,
        mission
    ):

        return {

            "mission":
            mission,

            "status":
            "active"
        }
      
