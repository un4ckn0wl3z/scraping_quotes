import requests

from pages.quotes_page import QuotesPage


class QuoteManager:
    """
    manager
    """

    def __init__(self, total_page):
        self.quote_items = []
        self.page_list = []
        self.total_page = total_page
        self._scrap()

    def _scrap(self):
        for i in range(1, self.total_page, 1):
            page_content = requests.get(f'http://quotes.toscrape.com/page/{i}').content
            self.page_list.append(page_content)

    @property
    def quotes(self):
        for page_item in self.page_list:
            page = QuotesPage(page_item)
            for quote in page.quotes:
                self.quote_items.append(quote)
        return self.quote_items
