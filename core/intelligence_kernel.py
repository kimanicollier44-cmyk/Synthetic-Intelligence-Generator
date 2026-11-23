class IntelligenceKernel:

    def __init__(
        self,
        router,
        memory,
        governor,
        planner
    ):

        self.router = router
        self.memory = memory
        self.governor = governor
        self.planner = planner

    def think(
        self,
        objective
    ):

        if not self.governor.evaluate(
            objective
        ):
            raise PermissionError()

        plan = (
            self.planner.create_plan(
                objective
            )
        )

        memory_context = (
            self.memory.load_memories()
        )

        response = (
            self.router.execute(
                "analysis",
                f"""
                Objective:
                {objective}

                Plan:
                {plan}

                Context:
                {memory_context}
                """
            )
        )

        return response
