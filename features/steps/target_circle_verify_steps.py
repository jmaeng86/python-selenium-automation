from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
STORY_BLOCK = (By.CSS_SELECTOR, "[data-test='storyblock-storyblockLinkWrapper']")

@given('Open Target Circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify 2 Circle story blocks are shown')
def verify_storyblocks_shown(context):
    story_blocks = context.driver.find_elements(*STORY_BLOCK)
    print(story_blocks)
    print(f'There are {len(story_blocks)} storyblocks shown')
    assert len(story_blocks) == 2, f'Expected 2 storyblocks, but got {len(story_blocks)}'