from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    Parser
    """

    def __init__(self, parent):
        self.parent = parent

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        self.parent.select_one(locator).string
