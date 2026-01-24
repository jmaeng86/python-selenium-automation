from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import Page

class Cart(Page):


    EMPTY_CART_TEXT = (By.XPATH,"//h1[contains(text(),'empty')]" )

    def verify_empty_cart(self):
        actual_text = self.driver.find_element(*self.EMPTY_CART_TEXT).text
        assert 'Your cart is empty' in actual_text, f'Expected text "Your cart is empty" not in actual text {actual_text}'

        