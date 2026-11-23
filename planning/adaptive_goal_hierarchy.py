class AdaptiveGoalHierarchy:

    def __init__(self):

        self.goals = {}

    def add_goal(
        self,
        goal_id,
        parent=None
    ):

        self.goals[goal_id] = {

            "parent": parent,

            "children": []
        }

        if parent:

            self.goals[parent][
                "children"
            ].append(goal_id)

    def descendants(
        self,
        goal_id
    ):

        return self.goals.get(
            goal_id,
            {}
        ).get(
            "children",
            []
        )
      
