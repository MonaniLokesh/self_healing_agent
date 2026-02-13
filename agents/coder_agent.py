from utils.llm import GeminiLLM
from utils.formatting import extract_code_block

llm = GeminiLLM()

CODER_PROMPT = """
You are a senior Python engineer.

Write clean, production-ready Python code.

Task:
{task}

Rules:
- Only return Python code without '```python' and '```'
- No explanations
"""


def generate_code(task: str) -> str:
    prompt = CODER_PROMPT.format(task=task)
    response = llm.generate(prompt)
    return extract_code_block(response)
