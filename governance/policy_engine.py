class PolicyEngine:

    def __init__(self):

        self.policies = []

    def add_policy(
        self,
        policy
    ):

        self.policies.append(
            policy
        )

    def evaluate(
        self,
        request
    ):

        for policy in self.policies:

            if not policy(request):

                return False

        return True
      
