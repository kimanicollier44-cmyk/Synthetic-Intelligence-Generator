class SelfModelEngine:

    def __init__(self):

        self.profile = {

            "capabilities": [],

            "limitations": [],

            "objectives": []
        }

    def add_capability(
        self,
        capability
    ):

        self.profile[
            "capabilities"
        ].append(capability)

    def add_limitation(
        self,
        limitation
    ):

        self.profile[
            "limitations"
        ].append(limitation)

    def self_description(self):

        return self.profile
      
