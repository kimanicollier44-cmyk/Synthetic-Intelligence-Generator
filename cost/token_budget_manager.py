class TokenBudgetManager:

    def __init__(
        self,
        monthly_limit
    ):

        self.monthly_limit = (
            monthly_limit
        )

        self.used_tokens = 0

    def consume(
        self,
        tokens
    ):

        if (
            self.used_tokens +
            tokens >
            self.monthly_limit
        ):

            raise RuntimeError(
                "Token budget exceeded"
            )

        self.used_tokens += tokens

    def remaining(self):

        return (
            self.monthly_limit -
            self.used_tokens
        )
      
