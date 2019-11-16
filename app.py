import requests

from pages.quotes_page import QuotesPage

page_content = requests.get('http://quotes.toscrape.com/').content
page = QuotesPage(page_content)
print('-' * 50)
for quote in page.quotes:
    print(quote.content)
    print(quote.author)
    print(quote.tags)
    print('-' * 50)
