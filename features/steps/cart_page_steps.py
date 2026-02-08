from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")


@when('Open cart page')
def open_cart(context):
    context.cart.open_cart_page()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.base_page(TOTAL_TXT,
        message='Subtotal text did not appear'
    )

    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify product in cart is correct')
def verify_product(context):
    context.base_page.verify_text(PRODUCT_NAME)



@then('Empty Cart message is shown')
def verify_empty_cart_msg(context):
    context.cart.verify_empty_cart()
