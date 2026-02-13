import google.generativeai as genai
from config.settings import GEMINI_API_KEY, MODEL_NAME


genai.configure(api_key=GEMINI_API_KEY)


class GeminiLLM:

    def __init__(self):
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
