class SemanticRouter:

    def __init__(
        self,
        routes
    ):

        self.routes = routes

    def classify(
        self,
        request
    ):

        request = request.lower()

        if "code" in request:

            return "coding"

        if "research" in request:

            return "research"

        if "image" in request:

            return "vision"

        return "general"

    def route(
        self,
        request
    ):

        category = self.classify(
            request
        )

        return self.routes.get(
            category
        )
      
