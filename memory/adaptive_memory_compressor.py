class AdaptiveMemoryCompressor:

    def compress(
        self,
        memories,
        max_items=100
    ):

        if len(memories) <= max_items:

            return memories

        return memories[
            -max_items:
        ]

    def summarize(
        self,
        memories
    ):

        return {

            "count":
            len(memories),

            "summary":
            "compressed memory"
        }
      
