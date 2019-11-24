from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    """
    Init
    """

    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotesPageLocators.QUOTE
        quotes_tags = self.browser.find_elements_by_css_selector(locator)
        return [QuoteParser(e) for e in quotes_tags]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.AUTHOR_DROPDOWN
        )
        return Select(element)

    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocators.TAG_DROPDOWN
        )
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(
            QuotesPageLocators.SEARCH_BUTTON
        )

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, selected_tag: str):
        self.tags_dropdown.select_by_visible_text(selected_tag)

    def search_for_quotes(self, author_name: str, tag: str) -> List[QuoteParser]:
        self.select_author(author_name)
        try:
            self.select_tag(tag)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author `{author_name}` does not have any question tagged with `{tag}`"
            )
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass
