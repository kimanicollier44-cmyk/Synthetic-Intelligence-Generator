import json
import os


class WorkflowRecovery:

    def __init__(
        self,
        path="state"
    ):

        self.path = path

        os.makedirs(
            path,
            exist_ok=True
        )

    def save_checkpoint(
        self,
        workflow_id,
        state
    ):

        file_path = (
            f"{self.path}/"
            f"{workflow_id}.json"
        )

        with open(
            file_path,
            "w"
        ) as file:

            json.dump(
                state,
                file,
                indent=2
            )

    def recover(
        self,
        workflow_id
    ):

        file_path = (
            f"{self.path}/"
            f"{workflow_id}.json"
        )

        if not os.path.exists(
            file_path
        ):
            return None

        with open(
            file_path,
            "r"
        ) as file:

            return json.load(file)
          
