from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[class*='cqLggv']")
    SIDEBAR_SIGNIN_BUTTON = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def open_main_page(self):
        self.open_url('https://www.target.com/')

    def click_account(self, *locator):
        self.ACCOUNT_BUTTON.click()

    def sidebar_signup(self,*locator):
        self.SIDEBAR_SIGNIN_BUTTON.click()

    def verify_signin_form(self,*locator):
        self.verify_text(*locator)



