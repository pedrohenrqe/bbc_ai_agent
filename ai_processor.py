import json
import ollama

from config import OLLAMA_MODEL


PROMPT = """
You are an English vocabulary extractor.

Your task:
- Extract useful intermediate/advanced English words.
- Ignore very basic words.
- Avoid proper nouns.
- Return EXACTLY 10 words.
- Each word must include:
  - word
  - portuguese translation
  - short example sentence in English

Return ONLY valid JSON.

Example:

[
  {
    "word": "breakthrough",
    "translation": "avanço",
    "example": "The company announced a major breakthrough."
  }
]
"""


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
                "content": text[:12000]
            }
        ]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except Exception:
        print("Erro ao interpretar JSON:")
        print(content)
        return []