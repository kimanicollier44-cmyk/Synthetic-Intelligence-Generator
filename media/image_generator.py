class ImageGenerator:

    def __init__(
        self,
        image_model
    ):

        self.model = image_model

    def generate(
        self,
        prompt,
        output_path
    ):

        image = self.model.generate(
            prompt
        )

        image.save(
            output_path
        )

        return output_path
      
