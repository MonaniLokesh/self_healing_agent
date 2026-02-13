from utils.llm import GeminiLLM

llm = GeminiLLM()

CODER_PROMPT = """
You are a senior Python engineer.

Write clean, production-ready Python code.

Task:
{task}

Rules:
- Only return Python code
- No explanations
"""


def generate_code(task: str) -> str:
    prompt = CODER_PROMPT.format(task=task)
    return llm.generate(prompt)
