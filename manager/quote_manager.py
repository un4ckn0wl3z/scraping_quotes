import requests

from pages.quotes_page import QuotesPage
from config.quote_config import QuoteConfig
from logger.app_logger import ApplicationLogger


class QuoteManager:
    """
    manager
    """

    def __init__(self, total_page=(QuoteConfig.TOTAL_PAGE+1)):
        self.quote_items = []
        self.page_list = []
        self.total_page = total_page
        self._scrap()

    def _scrap(self):
        for i in range(1, self.total_page, 1):
            url = f'{QuoteConfig.BASE_URL}/page/{i}'
            ApplicationLogger.inject(__name__).info(f'Scraping {url}')
            page_content = requests.get(url).content
            self.page_list.append(page_content)

    @property
    def quotes(self):
        for page_item in self.page_list:
            ApplicationLogger.inject(__name__).info(f'Got quote from page #{self.page_list.index(page_item)+1}')
            page = QuotesPage(page_item)
            for quote in page.quotes:
                ApplicationLogger.inject(__name__).info(f'Quote #{quote} from page #{self.page_list.index(page_item)+1} ')
                self.quote_items.append(quote)
        return self.quote_items
