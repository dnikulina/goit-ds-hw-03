import requests
from bs4 import BeautifulSoup
import json

current_url = "http://quotes.toscrape.com/"


def parse_quote_data(html):
    quote_store = []
    author_urls = set()

    if html.status_code == 200:
        soup = BeautifulSoup(html.content, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            quote_text = quote.find("span", class_="text")
            author = quote.find("small", class_="author")
            tags = quote.find_all("a", class_="tag")

            tags_list = []
            for tag in tags:
                tags_list.append(tag.text)

            quote_store.append(
                {
                    "tags": tags_list,
                    "author": author.text,
                    "quote": quote_text.text,
                }
            )

            author_url = quote.find("a")["href"]
            author_urls.add("http://quotes.toscrape.com" + author_url)

    return quote_store, author_urls


def parse_authors_data(html):
    if html.status_code == 200:
        soup = BeautifulSoup(html.content, "html.parser")

        author = soup.find("div", class_="author-details")

        fullname = author.find("h3", class_="author-title").text
        born_date = author.find("span", class_="author-born-date").text
        born_location = author.find("span", class_="author-born-location").text
        description = author.find("div", class_="author-description").text.strip()

        return {
            "fullname": fullname,
            "born_date": born_date,
            "born_location": born_location,
            "description": description,
        }


all_quotes = []
all_author_urls = set()


while current_url:
    response = requests.get(current_url)

    quotes, author_urls = parse_quote_data(response)

    all_quotes.extend(quotes)
    all_author_urls.update(author_urls)

    soup = BeautifulSoup(response.content, "html.parser")
    next_page = soup.find("li", class_="next")

    if next_page:
        current_url = "http://quotes.toscrape.com" + next_page.find("a")["href"]
    else:
        current_url = None


all_authors = []

for author_url in all_author_urls:
    response = requests.get(author_url)

    author = parse_authors_data(response)

    if author:
        all_authors.append(author)

with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(all_quotes, file, ensure_ascii=False, indent=4)

with open("authors.json", "w", encoding="utf-8") as file:
    json.dump(all_authors, file, ensure_ascii=False, indent=4)
