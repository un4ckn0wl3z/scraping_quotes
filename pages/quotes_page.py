

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    """
    Init
    """
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quotes_tags = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quotes_tags]
