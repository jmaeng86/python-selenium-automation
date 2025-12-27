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
sleep(2)
# Amazon logo
driver.find_element(By.XPATH, "//i[contains(@class,'a-icon-logo')]")

# Email field
driver.find_element(By.ID, "ap_email")

# Continue button
driver.find_element(By.ID, "continue")

# Conditions of Use link
driver.find_element(By.LINK_TEXT, "Conditions of Use")

# Privacy Notice link
driver.find_element(By.LINK_TEXT, "Privacy Notice")

# Help link
driver.find_element(By.LINK_TEXT, "Help")

# Need help signing in link
driver.find_element(By.LINK_TEXT, "Need help signing in?")

# Forgot your password link -not visible
#driver.find_element(By.LINK_TEXT, "Forgot your password")

# Other issues with Sign-In link -not visible
#driver.find_element(By.LINK_TEXT, "Other issues with Sign-In")

#Buying for work text?
driver.find_element(By.XPATH, "//*[contains(normalize-space(text()), 'Buying for work?')]")

#Shop on Amazon Business link
driver.find_element(By.LINK_TEXT, "Shop on Amazon Business")

# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

print("All Amazon Sign-In locators found successfully")
driver.quit()