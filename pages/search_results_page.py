from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")

    def verify_search_results(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TEXT).text
        assert 'tea' in actual_text, f'Expected text "tea" not in actual text {actual_text}'
