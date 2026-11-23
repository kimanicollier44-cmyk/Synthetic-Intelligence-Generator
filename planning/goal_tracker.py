class GoalTracker:

    def __init__(self):

        self.goals = {}

    def add_goal(
        self,
        goal_id,
        target
    ):

        self.goals[
            goal_id
        ] = {

            "target": target,

            "progress": 0
        }

    def update_progress(
        self,
        goal_id,
        progress
    ):

        if goal_id in self.goals:

            self.goals[
                goal_id
            ]["progress"] = progress

    def completed(
        self,
        goal_id
    ):

        goal = self.goals.get(
            goal_id
        )

        if not goal:
            return False

        return (
            goal["progress"] >=
            goal["target"]
        )
      
