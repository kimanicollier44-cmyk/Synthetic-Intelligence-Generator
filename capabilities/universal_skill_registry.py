class UniversalSkillRegistry:

    def __init__(self):

        self.skills = {}

    def register(
        self,
        skill_name,
        metadata
    ):

        self.skills[
            skill_name
        ] = metadata

    def get(
        self,
        skill_name
    ):

        return self.skills.get(
            skill_name
        )

    def discover(
        self
    ):

        return list(
            self.skills.keys()
        )
      
