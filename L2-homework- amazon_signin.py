from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Test Case: Users can navigate to SignIn page (Target)
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
options = Options()
options.add_argument("--incognito")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()




# Open Amazon Sign-In page
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(1)
# Amazon logo
driver.find_element(By.XPATH, "//a[contains(@class,'icon') and contains(@href,'logo')]")
sleep(1)
# Email field
driver.find_element(By.XPATH, "//input[@type='email']")
sleep(1)
# Continue button
driver.find_element(By.XPATH, "//span[@id='continue']")
sleep(1)
# Conditions of Use link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
sleep(1)
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
sleep(1)
# Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")
sleep(1)
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
sleep(1)
# Help link
driver.find_element(By.XPATH, "//a[@href='/help']")
sleep(1)
# Need help signing in link
driver.find_element(By.XPATH, "//a[contains(text(), 'Need help')]")
sleep(1)
# Forgot your password link -not visible
# Other issues with Sign-In link -not visible
#Buying for work text?
driver.find_element(By.XPATH, "//a[@href='/help']")
sleep(1)
#Shop on Amazon Business link
driver.find_element(By.XPATH, "//a[@id='ab-signin-ingress-link']")
sleep(1)
# Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
sleep(1)
print("All Amazon Sign-In locators found successfully")
#driver.quit()
