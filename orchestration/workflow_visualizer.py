class WorkflowVisualizer:

    def render(
        self,
        workflow
    ):

        lines = []

        for step in workflow:

            lines.append(
                f"[{step['order']}] "
                f"{step['name']}"
            )

        return "\n".join(lines)

    def graph(
        self,
        workflow
    ):

        result = "START\n"

        for step in workflow:

            result += (
                f"  |\n"
                f"  --> "
                f"{step['name']}\n"
            )

        result += "END"

        return result
      
