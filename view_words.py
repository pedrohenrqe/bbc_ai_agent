import sqlite3

DB_NAME = "words.db"

conn = sqlite3.connect(DB_NAME)

cursor = conn.cursor()

cursor.execute("""
    SELECT word, translation, example
    FROM words
    ORDER BY word ASC
""")

words = cursor.fetchall()

print("\nPALAVRAS SALVAS:\n")

for word, translation, example in words:
    print("=" * 50)
    print(f"Palavra: {word}")
    print(f"Tradução: {translation}")
    print(f"Exemplo: {example}")

conn.close()