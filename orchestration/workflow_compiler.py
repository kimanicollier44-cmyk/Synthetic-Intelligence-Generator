class WorkflowCompiler:

    def compile(
        self,
        workflow_definition
    ):

        compiled = []

        for step in workflow_definition:

            compiled.append({

                "name":
                step["name"],

                "agent":
                step["agent"],

                "order":
                step["order"]
            })

        return sorted(
            compiled,
            key=lambda x:
            x["order"]
        )
      
