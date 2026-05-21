import json
import re
import ollama

from config import OLLAMA_MODEL


PROMPT = """
Extract 10 intermediate English words from the text.

For each word return:
- word
- translation
- example

The example MUST be an English sentence using the word.

Example:

[
  {
    "word": "breakthrough",
    "translation": "avanço",
    "example": "The company announced a major breakthrough."
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
