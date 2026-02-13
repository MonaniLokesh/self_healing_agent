from utils.llm import GeminiLLM

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
    return llm.generate(prompt)
