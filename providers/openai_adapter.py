from openai import OpenAI


class OpenAIAdapter:

    def __init__(
        self,
        api_key,
        model="gpt-5"
    ):

        self.client = OpenAI(
            api_key=api_key
        )

        self.model = model

    def generate(
        self,
        prompt
    ):

        response = (
            self.client.responses.create(
                model=self.model,
                input=prompt
            )
        )

        return response.output_text
      
