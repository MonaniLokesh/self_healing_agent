from utils.llm import GeminiLLM
from utils.formatting import extract_code_block

llm = GeminiLLM()


TEST_PROMPT = """
You are a QA engineer.

Write pytest unit tests for this code.

Code:
{code}

Return only pytest code.
"""


def generate_tests(code: str) -> str:
    prompt = TEST_PROMPT.format(code=code)
    response = llm.generate(prompt)
    return extract_code_block(response)
