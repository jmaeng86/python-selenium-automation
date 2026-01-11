from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
ADD_TO_CART = (By.CSS_SELECTOR, "[aria-label*= 'Add PlayStation 5']")
SIDEBAR_ADD = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDEBAR_CLOSE = (By.CSS_SELECTOR, "[aria-label='close']")
SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
PLAYSTATION_TEXT =  (By.XPATH, "//*[contains(text(),'Playstation 5')]")

@when('Click first result')
def click_first_result(context):
    add_to_cart = context.driver.find_element(*ADD_TO_CART)
    add_to_cart.click()
    sleep(5)
@when('Click Add to cart on sidebar')
def click_add_to_cart(context):
    add_sidebar = context.driver.find_element(*SIDEBAR_ADD)
    add_sidebar.click()
    sleep(5)

@when('Close Sidebar')
def close_sidebar(context):
    sidebar_close = context.driver.find_element(*SIDEBAR_CLOSE)
    sidebar_close.click()
    sleep(5)


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    print(f'Expected text {expected_product} is in actual text {actual_text}')
    assert expected_product in actual_text, f'Expected text {expected_product} not in actual text {actual_text}'

@then('Verify {expected_product} is added to cart')
def verify_add_to_cart(context, expected_product):
    playstation_text = context.driver.find_element(*PLAYSTATION_TEXT).text
    print(f'Expected text {expected_product} is in actual text {playstation_text}')
    assert expected_product in playstation_text, f'Expected text {expected_product} not in actual text {playstation_text}'