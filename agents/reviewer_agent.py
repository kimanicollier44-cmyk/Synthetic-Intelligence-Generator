class ReviewerAgent:

    def __init__(self, model):
        self.model = model

    def review(
        self,
        content
    ):

        review_prompt = f"""
        Review this output.

        Criteria:

        - correctness
        - clarity
        - completeness
        - consistency

        Content:

        {content}

        Return improved version.
        """

        return self.model.generate(review_prompt)
      
