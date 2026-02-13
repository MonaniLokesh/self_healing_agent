from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME


class GeminiLLM:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=MODEL_NAME,
        )
        return chat_completion.choices[0].message.content
