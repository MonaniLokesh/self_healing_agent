import re

def extract_code_block(text: str) -> str:
    """
    Extracts the content of a markdown code block from the given text.
    If no code block is found, returns the original text stripped of whitespace.
    """
    pattern = r"```(?:\w+)?\s*(.*?)\s*```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    return text.strip()
