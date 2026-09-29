import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    
    authors = soup.find_all("small", class_="author")

    print("Quotes from the website:\n")

    for i, (quote, author) in enumerate(zip(quotes, authors), start=1):
        print(f"{i}. {quote.text}")
        print(f"   Author: {author.text}")
        print()
else:
    print("Failed to access the website.")