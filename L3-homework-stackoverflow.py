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




# Open stackoverflow page
driver.get("https://stackoverflow.com/users/signup")
sleep(600)
#Verify you are human
driver.find_element(By.CSS_SELECTOR, "[class='cb-i']").click()

# create account text
driver.find_element(By.CSS_SELECTOR, "div[class*='headline1'][")
sleep(1)
#terms of service
driver.find_element(By.CSS_SELECTOR, "[href='https://stackoverflow.com/legal/terms-of-service/public']")
sleep(1)
#privacy policy
driver.find_element(By.CSS_SELECTOR, "[href='https://stackoverflow.com/legal/privacy-policy']")
sleep(1)
# Email field
driver.find_element(By.CSS_SELECTOR, "#email")
sleep(1)
#password field
driver.find_element(By.CSS_SELECTOR, "#password")
sleep(1)
#password toggle
driver.find_element(By.CSS_SELECTOR, "[class*='js-show-password']")
sleep(1)
# signup button
driver.find_element(By.CSS_SELECTOR, "button#submit-button")
sleep(1)
#signin with google button
driver.find_element(By.CSS_SELECTOR,"button[class*='s-btn__google'")
sleep(1)
#sign up with github
driver.find_element(By.CSS_SELECTOR, "button[class*='s-btn__github'")
sleep(1)

#Get Stack Overflow for teams free for up to 50 users.
driver.find_element(By.CSS_SELECTOR, "[href='https://stackoverflow.com/teams?utm_source=so-owned&amp;utm_medium=product&amp;utm_campaign=free-50&amp;utm_content=public-sign-up']")
sleep(1)



print("All locators found successfully")
#driver.quit()
