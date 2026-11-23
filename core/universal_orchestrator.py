class UniversalOrchestrator:

    def __init__(
        self,
        cognitive_core,
        society_manager,
        planner,
        memory
    ):

        self.cognitive_core = (
            cognitive_core
        )

        self.society_manager = (
            society_manager
        )

        self.planner = planner

        self.memory = memory

    def execute(
        self,
        objective
    ):

        roadmap = (
            self.planner.create_roadmap(
                objective
            )
        )

        result = (
            self.cognitive_core.process(
                objective
            )
        )

        self.memory.store(
            objective
        )

        return {

            "objective":
            objective,

            "roadmap":
            roadmap,

            "result":
            result
        }
      
