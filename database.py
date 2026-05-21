import json
import os

FILE_NAME = "words.json"


def load_words():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_words(words):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(words, file, indent=4, ensure_ascii=False)


def word_exists(word):
    words = load_words()

    return any(
        item["word"].lower() == word.lower()
        for item in words
    )


def save_word(word, translation, example):
    words = load_words()

    if word_exists(word):
        return

    words.append({
        "word": word,
        "translation": translation,
        "example": example
    })

    save_words(words)