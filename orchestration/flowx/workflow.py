class Workflow:

    def __init__(self):
        self.steps = []

    def add_step(
        self,
        step_name,
        handler
    ):

        self.steps.append({
            "name": step_name,
            "handler": handler
        })

    def execute(
        self,
        payload
    ):

        result = payload

        for step in self.steps:

            result = stepresult
            

        return result
