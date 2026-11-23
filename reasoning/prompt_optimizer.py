class PromptOptimizer:

    def optimize(
        self,
        prompt
    ):

        optimized = prompt.strip()

        optimized += """

Requirements:
- be accurate
- cite assumptions
- verify logic
"""

        return optimized

    def compress(
        self,
        prompt,
        max_chars=4000
    ):

        return prompt[:max_chars]
