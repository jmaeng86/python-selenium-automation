from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

HELP_TEXT = (By.XPATH, "//h1[text()='Help']")
QUESTIONS = (By.XPATH, "//h2[contains(.,'question?')]")
BROWSE_ALL = (By.CSS_SELECTOR, "[class*='styles_ndsBaseButton__4Gp2_']")
SEARCH_BAR = (By.CSS_SELECTOR, "[id='helpSearch']")
WHAT_HELP_TEXT = (By.XPATH, "//h2[text()='What would you like help with?']")
HELP_GRID = (By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper']")
POPULAR_TEXT = (By.XPATH, "//h2[contains(text(),'Popular')]")
POPULAR_GRID = (By.CSS_SELECTOR, "[class*='LinkCard_linkListContainer__AwFOf']")



@given('Open Target help page')
def open_main(context):
    context.driver.get('https://help.target.com/help')
    sleep(1)
@then('Verify Help text appears at header')
def verify_title_text(context):
    title = context.driver.find_element(*HELP_TEXT).text
    print(f'{title} header found')
    assert title == 'Help', f'{title} header found'
    sleep(1)

@then('Verify Have a question')
def verify_question(context):
    question_text = context.driver.find_element(*QUESTIONS)
    actual = question_text.text
    print(f'{question_text} text found')
    assert actual == 'Have a question?', f'Expected Have a question? but got {actual}'
    sleep(1)

@then('Verify Browse all help')
def verify_browse_all(context):
    browse_btn = context.driver.find_element(*BROWSE_ALL)
    print(f'{browse_btn.text} button found')
    sleep(1)

@then('Verify Help Search Bar')
def verify_search(context):
    search_bar = context.driver.find_element(*SEARCH_BAR)
    print(f'{search_bar.text} search bar found')
    sleep(1)

@then('Verify What would you like help with')
def verify_what(context):
    what_help_text = context.driver.find_element(*WHAT_HELP_TEXT)
    print(f'{what_help_text.text} text found')
    sleep(1)

@then('Verify all elements within grid')
def verify_grid(context):
    all_elements = context.driver.find_elements(*HELP_GRID)
    print(f'{len(all_elements)} elements found')
    sleep(1)

@then('Verify Popular title text')
def verify_sub_title(context):
    popular_text = context.driver.find_elements(*POPULAR_TEXT)
    print(f'{popular_text} text found')
    sleep(1)

@then('Verify All popular pages')
def verify_popular_pages(context):
    popular_pages = context.driver.find_elements(*POPULAR_GRID)
    print(f'{popular_pages} popular pages  found')
    sleep(1)



