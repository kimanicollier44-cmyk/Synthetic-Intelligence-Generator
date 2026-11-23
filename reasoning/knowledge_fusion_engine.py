class KnowledgeFusionEngine:

    def fuse(
        self,
        sources
    ):

        fused = []

        seen = set()

        for source in sources:

            for item in source:

                if item not in seen:

                    seen.add(item)

                    fused.append(item)

        return fused

    def summarize(
        self,
        model,
        knowledge
    ):

        prompt = (
            "Combine the "
            "following knowledge:\n\n"
            f"{knowledge}"
        )

        return model.generate(
            prompt
        )
      
