class MultimodalAgent:

    def __init__(
        self,
        vision_model,
        language_model
    ):

        self.vision_model = (
            vision_model
        )

        self.language_model = (
            language_model
        )

    def analyze_image(
        self,
        image_path
    ):

        visual_context = (
            self.vision_model
            .analyze(image_path)
        )

        return (
            self.language_model
            .generate(
                f"""
                Explain
                the image.

                {visual_context}
                """
            )
        )
      
