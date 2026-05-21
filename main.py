from scraper import (
    get_article_links,
    extract_article_text
)

from ai_processor import extract_words

from database import (
    create_database,
    word_exists,
    save_word
)


def main():
    create_database()

    print("\nBuscando artigos da BBC Technology...\n")

    links = get_article_links()

    all_text = ""

    for link in links:
        print(f"Lendo: {link}")

        text = extract_article_text(link)

        all_text += text + "\n"

    print("\nProcessando com IA local...\n")

    words = extract_words(all_text)

    saved_count = 0

    for item in words:
        word = item["word"].strip().lower()
        translation = item["translation"].strip()
        example = item["example"].strip()

        if not word_exists(word):
            save_word(word, translation, example)

            saved_count += 1

            print("=" * 50)
            print(f"Palavra: {word}")
            print(f"Tradução: {translation}")
            print(f"Exemplo: {example}")

    print("\n")
    print(f"{saved_count} novas palavras salvas.")


if __name__ == "__main__":
    main()