import requests

from pages.quotes_page import QuotesPage

page_list = []
for i in range(1, 11, 1):
    page_content = requests.get(f'http://quotes.toscrape.com/page/{i}').content
    page_list.append(page_content)

for page_item in page_list:
    page = QuotesPage(page_item)
    print('-' * 50)
    for quote in page.quotes:
        print(quote.content)
        print(quote.author)
        print(quote.tags)
        print('-' * 50)
