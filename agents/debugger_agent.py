from utils.llm import GeminiLLM
from utils.formatting import extract_code_block

llm = GeminiLLM()


DEBUG_PROMPT = """
Fix the Python code using failing test logs.

Code:
{code}

Logs:
{logs}

Return only corrected Python code.
"""


def debug_code(code, logs):
    prompt = DEBUG_PROMPT.format(code=code, logs=logs)
    response = llm.generate(prompt)
    return extract_code_block(response)
