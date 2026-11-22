class ResearchAgent:

    def __init__(self, model):
        self.model = model

    def run(self, request):

        prompt = f"""
        Research the following topic.

        Topic:
        {request}

        Return:
        - key facts
        - important concepts
        - useful context
        """

        return self.model.generate(prompt)
      
