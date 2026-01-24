from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_target(context):
    context.app.main_page.open_main_page()

@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_button()

@then('Verify Your cart is empty message is shown')
def verify_empty_cart(context):
    context.app.cart.verify_empty_cart()



#@when('Click Sign In')
#def click_sign_in(context):
#    context.driver.find_element(By.CSS_SELECTOR,"span.iyNjUL").click()
#
#
#@when('From right side navigation menu, click Sign In')
#def menu_sign_in(context):
#    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
#
#@then('Verify Sign In form opened')
#def verify_sign_in(context):
#    expected_text = 'Sign in or create account'
#    actual_text = context.driver.find_element(By.XPATH,"//h1[text()='Sign in or create account']").text
#    print(actual_text)
#    assert expected_text == actual_text, (f'Expected text {expected_text} not in actual text {actual_text}')
