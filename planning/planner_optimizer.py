class PlannerOptimizer:

    def optimize(
        self,
        plan
    ):

        optimized = []

        visited = set()

        for step in plan:

            if step not in visited:

                optimized.append(
                    step
                )

                visited.add(
                    step
                )

        return optimized

    def prioritize(
        self,
        plan
    ):

        return sorted(
            plan,
            key=lambda x:
            x.get(
                "priority",
                999
            )
        )
      
