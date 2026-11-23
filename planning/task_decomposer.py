class TaskDecomposer:

    def __init__(
        self,
        model
    ):
        self.model = model

    def decompose(
        self,
        objective
    ):

        prompt = f"""
        Break the objective into
        executable tasks.

        Objective:
        {objective}

        Return:
        - task list
        - dependencies
        - priorities
        """

        return self.model.generate(
            prompt
        )

    def validate(
        self,
        tasks
    ):

        return len(tasks) > 0
