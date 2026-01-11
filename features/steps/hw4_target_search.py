from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle')
def open_target(context):
    context.driver.get('http://target.com/circle')


