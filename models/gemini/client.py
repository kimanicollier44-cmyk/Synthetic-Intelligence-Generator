import google.generativeai as genai

class GeminiClient:

    def __init__(self, api_key=None):
        if api_key:
            genai.configure(api_key=api_key)

    def generate(self, prompt):
        model = genai.GenerativeModel("gemini")
        response = model.generate_content(prompt)
        return response.text
