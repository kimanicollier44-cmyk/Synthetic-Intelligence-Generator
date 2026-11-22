from anthropic import Anthropic


class AnthropicAdapter:

    def __init__(
        self,
        api_key,
        model
    ):

        self.client = Anthropic(
            api_key=api_key
        )

        self.model = model

    def generate(
        self,
        prompt
    ):

        message = (
            self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        return (
            message.content[0].text
        )
      
