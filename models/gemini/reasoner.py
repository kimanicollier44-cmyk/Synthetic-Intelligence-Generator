class ExtendedReasoner:

    def __init__(self, model):
        self.model = model

    def think(self, task):

        reasoning_prompt = f"""
        Analyze the task.

        Task:
        {task}

        Follow:

        1. Understand objective
        2. Break into subtasks
        3. Evaluate options
        4. Produce best plan
        """

        return self.model.generate(
            reasoning_prompt
        )
