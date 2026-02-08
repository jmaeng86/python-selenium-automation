from selenium.webdriver.common.by import By
from time import sleep


from pages.base_page import Page

class Cart(Page):


    EMPTY_CART_TEXT = (By.XPATH,"//h1[contains(text(),'empty')]" )

    def open_cart_page(self):
        self.open_url('https://www.target.com/cart')






    def verify_empty_cart(self):
        self.verify_partial_text('your cart is empty',*self.empty_cart_msg)
        self.verify_url('https://www.target.com/cart')
        self.verify_url_contains('cart')

