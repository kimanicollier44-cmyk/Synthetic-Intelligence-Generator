import uuid


class ObjectiveManager:

    def __init__(self):

        self.objectives = {}

    def create(
        self,
        title,
        description
    ):

        objective_id = str(
            uuid.uuid4()
        )

        self.objectives[
            objective_id
        ] = {

            "title": title,

            "description":
            description,

            "status":
            "active"
        }

        return objective_id

    def get(
        self,
        objective_id
    ):

        return self.objectives.get(
            objective_id
        )

    def close(
        self,
        objective_id
    ):

        if objective_id in self.objectives:

            self.objectives[
                objective_id
            ]["status"] = "closed"
