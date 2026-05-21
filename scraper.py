import requests
from bs4 import BeautifulSoup

from config import BBC_TECH_URL


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def get_article_links():
    response = requests.get(BBC_TECH_URL, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/news/articles/" in href:
            if href.startswith("/"):
                href = "https://www.bbc.com" + href

            links.add(href)

    return list(links)[:5]


def extract_article_text(url):
    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    text = []

    for p in paragraphs:
        content = p.get_text(strip=True)

        if len(content) > 40:
            text.append(content)

    return " ".join(text)