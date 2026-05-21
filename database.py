import sqlite3

DB_NAME = "words.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE,
            translation TEXT,
            example TEXT
        )
    """)

    conn.commit()
    conn.close()


def word_exists(word):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM words WHERE LOWER(word) = LOWER(?)",
        (word,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_word(word, translation, example):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO words(word, translation, example)
        VALUES (?, ?, ?)
    """, (word, translation, example))

    conn.commit()
    conn.close()