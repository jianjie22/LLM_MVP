# app/anonymizer.py

import re

def anonymize_text(text: str) -> str:
    text = re.sub(r"\b[\w.-]+?@\w+?\.\w+?\b", "[EMAIL]", text)
    text = re.sub(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b", "[NAME]", text)
    return text
