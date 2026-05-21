import json
import re
import ollama

from config import OLLAMA_MODEL


PROMPT = """
Extract exactly 10 intermediate or advanced English words from the text.

Rules:
- Avoid basic words
- Avoid proper nouns
- Avoid repeated words
- Return ONLY valid JSON
- Do not write explanations
- Do not use markdown

Format:

[
  {
    "word": "example",
    "translation": "exemplo",
    "example": "This is an example sentence."
  }
]
"""


def extract_json(text):
    match = re.search(r"\[.*\]", text, re.DOTALL)

    if not match:
        return []

    try:
        return json.loads(match.group())
    except Exception:
        return []

def extract_words(text):
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": text[:8000]
            }
        ]
    )

    content = response["message"]["content"]

    print("\nRESPOSTA DA IA:\n")
    print(content)

    return extract_json(content)
