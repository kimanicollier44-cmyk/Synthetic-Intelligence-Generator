class CognitiveCore:

    def __init__(
        self,
        orchestrator,
        memory,
        reasoner,
        planner
    ):

        self.orchestrator = orchestrator
        self.memory = memory
        self.reasoner = reasoner
        self.planner = planner

    def process(
        self,
        objective
    ):

        plan = (
            self.planner
            .create_roadmap(
                objective
            )
        )

        reasoning = (
            self.reasoner
            .think(
                objective
            )
        )

        context = (
            self.memory
            .retrieve(
                objective
            )
        )

        result = (
            self.orchestrator
            .execute(
                objective
            )
        )

        return {

            "objective":
            objective,

            "plan":
            plan,

            "reasoning":
            reasoning,

            "context":
            context,

            "result":
            result
        }
      
