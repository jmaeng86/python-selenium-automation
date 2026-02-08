from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[class*='cqLggv']")
SIDEBAR_SIGNIN_BUTTON = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
SIGN_IN_HEADER = (By.CSS_SELECTOR, "[class*='h-text-center']")

@given('Open target.com')
def open_target(context):
    context.app.main_page.open_main_page()

@when('Click Sign in')
def click_signin(context):
    context.app.main_page.click_account()

@when('Click Sidebar sign in')
def click_sidebar_signup(context):
    context.app.main_page.sign_in_sidebar()

@then('Verify Your cart is empty message is shown')
def verify_signin_form(context):
    context.app.main_page.verify_text(SIGN_IN_HEADER)