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



# 1. Open page
driver.get("https://www.target.com/")
sleep(2)

# 2. Click Account button
driver.find_element(By.XPATH, "//span[text()='Account']").click()
sleep(2)

# 4. Verify SignIn page opened
header = driver.find_element(By.XPATH,"//button[contains(text(),'Sign in')]")
header.click()
print("Sign in text visible:", header.text)
# 3. Click SignIn button

#driver.find_element(By.XPATH, "//button[text()='Sign in or create account']").click()
#sleep(2)


# SignIn button is shown

driver.find_element(By.XPATH, "//button[text()='Continue']")
print("Sign-in button found")

driver.quit()




