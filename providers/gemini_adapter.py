import google.generativeai as genai


class GeminiAdapter:

    def __init__(
        self,
        api_key,
        model_name
    ):

        genai.configure(
            api_key=api_key
        )

        self.model = (
            genai.GenerativeModel(
                model_name
            )
        )

    def generate(
        self,
        prompt
    ):

        response = (
            self.model
            .generate_content(
                prompt
            )
        )

        return response.text
      
